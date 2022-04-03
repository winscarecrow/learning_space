def menu(name):
    print("สวัสดี", name, """กรุณาเลือกทำรายการ
1.แสดงข้อมูลสมาชิก
2.เพิ่มข้อมูลสมาชิก
3.สรุปข้อมูลโควิด
4.ออกจากโปรแกรม
""")

def showdata(mem):
    if len(mem) == 0:
        print("ยังไม่มีการเพิ่มข้อมูลเข้ามา")
    else:
        print("ชื่อ \t อายุ \t การติดเชื้อ")
        for i in mem:
            print(f'{i} \t {mem[i]["Age"]} ปี \t {mem[i]["Covid"]}')

def adddata():
    num = (1, 2)
    infect = ("เคย", "ไม่เคย")
    total = int(input("จำนวนสมาชิกที่ต้องการเพิ่ม: "))
    for i in range(total):
        print(f"สมาชิกคนที่ {i + 1}")
        name = input("กรุณาระบุชื่อสมาชิก: ")
        age = int(input("กรุณาระบุอายุ: "))
        covid = int(input("เคยติดโควิดหรือไม่\n1.เคย\n2.ไม่เคย\n>>> "))
        members[name] = {"Age": age, "Covid": infect[num.index(covid)]}

def summary(mem):
    familyMember = len(mem)
    infect = 0
    for i in mem.values():
        if i["Covid"] == "เคย":
            infect += 1
    elder = 0
    for i in mem.values():
        if (i["Age"] > 59) and (i["Covid"] == "เคย"):
            elder += 1
    print("สมาชิก(คน) \t เคยติดโควิด(คน) \t ผู้สูงอายุที่เคยติดโควิด(คน)")
    print(f"{familyMember} \t\t {infect} \t\t {elder}")

members = {}
again = "y"
name = input("กรุณาใส่ชื่อของคุณ: ")

while again == "y":
    menu(name)
    choice = int(input("เลือกทำรายการ (1-4): "))
    if choice == 1:
        showdata(members)
    elif choice == 2:
        adddata()
    elif choice == 3:
        summary(members)
    elif choice == 4:
        again = "n"
    else :
        print("คุณเลือกทำรายการไม่ถูกต้อง")