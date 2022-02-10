### library ###
import mysql.connector as sqlcnt
from os import system


### database config ###
mydb = sqlcnt.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "pythoncompany_data"
)


### function ###
def addData(): # Name, Surname, Age
	columns = ["First Name", "Last Name", "Age"]
	user_profiles = [input(f"Enter {columns[i]}: ") for i in range(3)]

	obj_mycursor = mydb.cursor()
	insert_script = "INSERT INTO UserProfile(FirstName, LastName, Age) VALUES(%s, %s, %s)"
	insert_value = (data for data in user_profiles)
	obj_mycursor.execute(insert_script, insert_value)
	obj_mycursor.commit()

	print(obj_mycursor.rowcount, "record inserted.")


def showData():
	obj_mycursor = mydb.cursor()
	obj_mycursor.execute("SELECT * FROM UserProfile")
	dt_data = obj_mycursor.fetchall()

	for row_data in dt_data:
		print(row_data)


### main program ###
system('cls')
print("----- Profiles Report Program -----")

onoff = 1
while onoff:

	print("""----- MENU -----
  [1] Create Profile
  [2] Show Report
  [Q] Exit Program
""")
	
	selectMenu = input("Select Menu: ")
	if selectMenu in ("1", "2"):
		match selectMenu:
			case "1":
				addData()
			case "2":
				showData()

		again = input("Run Program Again? (Y/N): ")
		if again.upper() != "Y":
			onoff = 0

	elif selectMenu.upper() == "Q":
		break

	else:
		print("\nInvalid Input !, Please Select Again\n")

print("Program Closed")
