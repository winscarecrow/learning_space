import csv
from datetime import datetime as dt
from os import system
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
		print("""---- Employee Management ----
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
						print(row_data)

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
						columns = ["Employee ID", "First Name", "Last Name", "Weight", "Height"]
						print("---- Select Column to Edit ----")
						for e,i in enumerate(columns):
							print(f"[{e}] {i}")
						edit_condition = ["Edit Column", "New Value", "Employee ID"]
						edit_profile = tuple(input(f"Enter {edit_condition[i]}: ") for i in range(3))
						edit_script = "UPDATE EmployeeProfile SET %s = %s WHERE EmployeeId = %s"
						obj_mycursor.execute(edit_script, edit_profile)
						mydb.commit()
						print(obj_mycursor.rowcount, "record edited.")
					except:
						print("Something Wrong!")

				case "4":
					try:
						print("---- Delete Employee ----")
						delete_profile = tuple(input(f"Enter Employee ID: ") for i in range(1))
						delete_script = "DELETE FROM EmployeeProfile WHERE EmployeeId = %s"
						obj_mycursor.execute(delete_script, delete_profile)
						mydb.commit()
						print(obj_mycursor.rowcount, "record deleted.")
					except:
						print("Something Wrong!")

		elif menu.upper() == "B":
			print("\nBack to Main Menu\n")
			break

		else:
			print("\nInvalid Input!\n")

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
				pass
			case "3":
				pass
	elif mainMenu.upper() == "Q":
		print("\nProgram Closed")
		break
	else:
		print("\nInvalid Input!\n")
