from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector as sqlcnt

################################### GUI
root = Tk()
root.title('User Profile Report')
root.geometry('800x500')

################################### mysql Config
mydb =  sqlcnt.connect(
	host = "localhost",
	user = "root",
	password = "",
	database = "pythoncompany_data"
)

################################### Tk Config
text_font = ('Consolas',18)

Bfont = ttk.Style()
Bfont.configure('TButton', font=('Consolas',12))

################################### Tab Setting
Tab = ttk.Notebook(root)
Tab.pack(fill=BOTH, expand=True)

Tab_1 = Frame(Tab)
Tab_2 = Frame(Tab)

Tab.add(Tab_1, text='Create')
Tab.add(Tab_2, text='Report')

################################### Tab 1 Function
def InsertValue():
	try:
		user_profile = (T1_var_1.get(), T1_var_2.get(), T1_var_3.get())
		obj_mycursor = mydb.cursor()
		insert_script = "INSERT INTO UserProfile(FirstName, LastName, Age) VALUES(%s, %s, %s)"
		obj_mycursor.execute(insert_script, user_profile)
		mydb.commit()

		for vs in var_store:
			vs.set('')

		messagebox.showinfo('Result Box', f'{obj_mycursor.rowcount} record inserted.')
		
	except:
		messagebox.showwarning('Warning !', 'Something Wrong !\nPlease Check Your Input')

################################### Tab 1 Main
T1_masterFrame = Frame(Tab_1)
T1_masterFrame.pack(pady=25)

column = ['Name', 'Surname', 'Age']
T1_var_1, T1_var_2, T1_var_3 = StringVar(), StringVar(), StringVar()
var_store = [T1_var_1, T1_var_2, T1_var_3]

for e,cl in enumerate(column):
	T1_label = Label(T1_masterFrame, text=cl, font=text_font)
	T1_label.grid(row=e , column=0, pady=15)
	T1_entry = Entry(T1_masterFrame, textvariable=var_store[e], width=25, font=('Leelawadee UI', 14))
	T1_entry.grid(row=e, column=1, padx=25)

T1_button = ttk.Button(Tab_1, text='OK', command=InsertValue)
T1_button.pack(ipadx=15, ipady=8, pady=40)

################################### Tab 2 Function
def UpdateTable():
	obj_mycursor = mydb.cursor()
	obj_mycursor.execute("SELECT * FROM UserProfile")
	get_db = obj_mycursor.fetchall()

	T2_treeview.delete(*T2_treeview.get_children())
	for vl in get_db:
		T2_treeview.insert('', 'end', value=[ vl[0], vl[1], vl[2], vl[3], vl[4] ])

################################### Tab 2 Main
T2_masterFrame = Frame(Tab_2)
T2_masterFrame.pack(pady=25)

headers = ['IdNo', 'Name', 'Surname', 'Age', 'CreateDate']
headers_width = [50, 200, 200, 50, 200]
T2_treeview = ttk.Treeview(T2_masterFrame, columns=headers, show='headings', height=15)
T2_treeview.pack()

for hd,hw in zip(headers,headers_width):
	T2_treeview.heading(hd, text=hd)
	T2_treeview.column(hd, width=hw)


T2_button = ttk.Button(Tab_2, text='Search', command=UpdateTable)
T2_button.pack(ipadx=15, ipady=8, pady=20)

################################### Run Program
root.mainloop()
