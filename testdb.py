import sqlite3
import csv
from datetime import datetime as dt

con = sqlite3.connect('D:\\Downloads\\DB.Browser.for.SQLite-3.12.2-win64\\example.db')
cur = con.cursor()

colName = ["EmployeeId", "FirstName", "LastName", "Weight", "Height"]

def dataInsert():
	insData = [ input(f"Enter {colName[i]}: ") for i in range(len(colName)) ]
	cd = dt.now().strftime("%Y-%m-%d %H:%M:%S")
	insData.append(cd)
	insData = tuple(insData)

	cur.execute("INSERT INTO EmployeeProfile(EmployeeId, FirstName, LastName, Weight, Height, CreateDate) VALUES(?, ?, ?, ?, ?, ?)", insData)
	con.commit()

	print("1 row inserted")


def dataSelect():
	myCur = cur.execute("SELECT EmployeeId, FirstName, LastName, Weight, Height, CreateDate FROM EmployeeProfile ORDER BY ProfileId ASC")
	for row in myCur:
		print(f"EmpID:'{row[0]}' Name:'{row[1]}' Surname:'{row[2]}' Weight:'{row[3]}' Height:'{row[4]}' CreateDate:'{row[5]}'")


def dataUpdate():
	colName = ["Column Name", "Edit Value", "Condition", "Condition Value"]
	editData = [ input(f"Enter {colName[i]}: ") for i in range(len(colName)) ]
	value = (editData[1], editData[3])

	cur.execute(f"UPDATE EmployeeProfile SET {editData[0]} = ? WHERE {editData[2]} = ?", value)
	con.commit()

	print("1 row updated")


def ExportCSV():
	cur.execute("SELECT EmployeeId, FirstName, LastName, Weight, Height, CreateDate FROM EmployeeProfile ORDER BY ProfileId")
	dt_data = cur.fetchall()
	values = [list(i) for i in dt_data]
	for i in range(len(values)):
		values[i].insert(5, round(float(values[i][3]) / ((float(values[i][4])*0.01)**2), 1))
		if values[i][5] < 18.5:
			values[i].insert(6, "Underweight")
		elif (values[i][5] >= 18.5) and (values[i][5] <= 24.9):
			values[i].insert(6, "Normal")
		elif (values[i][5] >= 25.0) and (values[i][5] <= 29.9):
			values[i].insert(6, "Overweight")
		else:
			values[i].insert(6, "Obesity")

	ymd = dt.now().strftime("%y%m%d")
	with open(f"Employee_Healthy_{ymd}.csv", "w", newline="", encoding="utf-8") as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for i in values:
			writer.writerow(i)

	print("\nExport file Success\n")



