import csv
from os import system
from datetime import datetime as dt
import mysql.connector as sqlcnt

####################################

mydb = sqlcnt.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "pythoncompany_data"
)

obj_mycursor = mydb.cursor()

####################################

def EmpMan():
	while True:
		print("""
---- Employee Management ----
	[1] Show Employee Profile
	[2] Create Employee Profile
	[3] Edit Employee Profile
	[4] Delete Employee Profile
	[B] Back to Main Menu
""")

		menu = input("Select Menu: ")
		if menu in ["1", "2", "3", "4"]:

			match menu:
				case "1":
					obj_mycursor.execute("SELECT * FROM EmployeeProfile")
					dt_data = obj_mycursor.fetchall()
					for row_data in dt_data:
						temp = [row_data[i] for i in range(6)]
						dt_stamp = row_data[6].strftime("%x %X")
						temp.append(dt_stamp)
						print(temp)

				case "2":
					try:
						columns = ["Employee ID", "First Name", "Last Name", "Weight", "Height"]
						user_profile = tuple(input(f"Enter {columns[i]}: ") for i in range(len(columns)))
						insert_script = "INSERT INTO EmployeeProfile(EmployeeId, FirstName, LastName, Weight, Height) VALUES(%s, %s, %s, %s, %s)"
						obj_mycursor.execute(insert_script, user_profile)
						mydb.commit()
						print(obj_mycursor.rowcount, "record inserted.")
					except:
						print("Something Wrong!")

				case "3":
					try:
						columns = {1:"Employee ID", 2:"First Name", 3:"Last Name", 4:"Weight", 5:"Height"}
						print("---- Select Column to Edit ----")
						for i in columns.items():
							print(i)
						clm = int(input("Edit Column: "))
						edit_condition = ["New Value", "Employee ID"]
						edit_profile = tuple(input(f"Enter {edit_condition[i]}: ") for i in range(2))
						edit_script = f"UPDATE EmployeeProfile SET {columns[clm]} = %s WHERE EmployeeId = %s"
						obj_mycursor.execute(edit_script, edit_profile)
						mydb.commit()
						print(obj_mycursor.rowcount, "record edited.")
					except:
						print("Something Wrong!")

				case "4":
					try:
						print("---- Delete Employee ----")
						delete_profile = input(f"Enter Employee ID: ")
						delete_script = "DELETE FROM EmployeeProfile WHERE EmployeeId = %s"
						obj_mycursor.execute(delete_script, (delete_profile,))
						mydb.commit()
						print(obj_mycursor.rowcount, "record deleted.")
					except:
						print("Something Wrong!")

		elif menu.upper() == "B":
			print("\nBack to Main Menu\n")
			break

		else:
			print("\nInvalid Input!\n")


def BMICal():
	while True:
		print("""
---- BMI Report ----
	[1] Show All Employee BMI
	[2] Select Employee
	[B] Back to Main Menu
""")

		menu = input("Select Menu: ")
		if menu in ["1", "2"]:
 
			match menu:
				case "1":
					obj_mycursor.execute("SELECT EmployeeId, FirstName, LastName, Weight, Height FROM EmployeeProfile ORDER BY ProfileId")
					dt_data = obj_mycursor.fetchall()
					values = [list(i) for i in dt_data]
					for i in range(len(values)):
						values[i].append(round(float(values[i][3]) / ((float(values[i][4])*0.01)**2), 1))
						if values[i][5] < 18.5:
							values[i].append("Underweight")
						elif (values[i][5] >= 18.5) and (values[i][5] <= 24.9):
							values[i].append("Normal")
						elif (values[i][5] >= 25.0) and (values[i][5] <= 29.9):
							values[i].append("Overweight")
						else:
							values[i].append("Obesity")
					for row in values:
						print(f"EmpID:{row[0]}, Name:{row[1]}, Surname:{row[2]}, Weight:{row[3]}kg., Height:{row[4]}cm., BMI:{row[5]}, Result:{row[6]}")

				case "2":
					empid = input("Enter Employee: ")
					select_script = "SELECT EmployeeId, FirstName, LastName, Weight, Height FROM EmployeeProfile WHERE EmployeeId = %s"
					obj_mycursor.execute(select_script, (empid,))
					dt_data = obj_mycursor.fetchall()
					values = []
					for i in dt_data:
						for j in i:
							values.append(j)
					values.append(round(float(values[3]) / ((float(values[4])*0.01)**2), 1))
					if values[5] < 18.5:
						values.append("Underweight")
					elif (values[5] >= 18.5) and (values[5] <= 24.9):
						values.append("Normal")
					elif (values[5] >= 25.0) and (values[5] <= 29.9):
						values.append("Overweight")
					else:
						values.append("Obesity")
					print(f"EmpID:{values[0]}, Name:{values[1]}, Surname:{values[2]}, Weight:{values[3]}kg., Height:{values[4]}cm., BMI:{values[5]}, Result:{values[6]}")


		elif menu.upper() == "B":
			print("\nBack to Main Menu\n")
			break

		else:
			print("\nInvalid Input!\n")


def ExportCSV():
	obj_mycursor.execute("SELECT EmployeeId, FirstName, LastName, Weight, Height, CreateDate FROM EmployeeProfile ORDER BY ProfileId")
	dt_data = obj_mycursor.fetchall()
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

####################################

system('cls')

while True:
	print("""---- Health Report Program ----
	[1] Employee Management
	[2] Employee BMI Result
	[3] Export CSV
	[Q] Exit Program
""")
	
	mainMenu = input("Select Menu: ")

	if mainMenu in ["1", "2", "3"]:
		match mainMenu:
			case "1":
				EmpMan()
			case "2":
				BMICal()
			case "3":
				ExportCSV()

	elif mainMenu.upper() == "Q":
		print("\nProgram Closed")
		break

	else:
		print("\nInvalid Input!\n")
