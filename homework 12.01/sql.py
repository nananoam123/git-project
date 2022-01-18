import sqlite3

conn=sqlite3.connect('C:\\Users\\Noam Daloya\\Desktop\\Devops Project\\SQL\\test.db')

#task 1
#name = input("Type the worker's 'Name' : ")
# if  name[0].islower():
#     print("That's not the appropriate way to type a name but we fixed it for you")
#     name.title()
# age =int(input ("Type the worker's Age :"))
# while age > 67 or age < 18 :
#     print('Type an age between 67-18')
#     age = int(input("Type the worker's Age :"))
# Address=input("Type the worker's Address :")
# Salary =input("Type the worker's Salary :")
#
# def addNewWorker():
#  conn.execute(f"INSERT INTO COMPANY(NAME,AGE,ADDRESS,SALARY) VALUES ('{name}',{age},'{Address}',{Salary});")
#  conn.commit()
#  fet=conn.execute("SELECT * FROM COMPANY ORDER BY ID DESC LIMIT 1")
#  print(fet.fetchone())
# addNewWorker()

#task2
# rd=''
# dups= set()
# tes=[]
# tesid=[]
# search = input("Where should i search 'AGE','NAME','ADDRESS','SALARY' ? :").upper()
# while search != 'AGE' and search != 'NAME' and search != 'ADDRESS' and search != 'SALARY':
#     print('Search field does not exist')
#     search = input("Where should i search 'AGE','NAME','ADDRESS','SALARY' ? :").upper()
# row=conn.execute(f"SELECT * FROM COMPANY where {search} = (SELECT {search} from company GROUP by {search} HAVING count ({search})>1);")
# for r in row :
#     tes.append(r)
# print(tes)
# option = int(input("type the entry 'ID' you want to keep? :"))
# for t in tes :
#    id=(t[0])
#    tesid.append(id)
# tesid.remove(option)
# for i in tesid :
#     conn.execute(f"DELETE FROM COMPANY WHERE ID ='{i}'")
#     conn.commit()
#task 3

#
# wname = input("Type the worker's 'Name' : ")
# name=conn.execute("SELECT * FROM COMPANY ")
# for n in name :
#     while wname in n :
#         print (n)
#         print('This name is already in the db ')
#         choice=input("Do you want to update the current one ? 'y' or 'n'")
#         if choice == 'y':
#             age = int(input("Type the worker's Age :"))
#             Address = input("Type the worker's Address :")
#             Salary = input("Type the worker's Salary :")
#             conn.execute(f"UPDATE COMPANY SET NAME='{wname}',AGE={age},ADDRESS='{Address}',SALARY={Salary} where id='{n[0]}'")
#             conn.commit()
#         if choice == 'n':
#             print('Ok you choose not to update')
#             quit()
# age =int(input ("Type the worker's Age :"))
# Address=input("Type the worker's Address :")
# Salary =input("Type the worker's Salary :")
#
# def addNewWorker():
#  conn.execute(f"INSERT INTO COMPANY(NAME,AGE,ADDRESS,SALARY) VALUES ('{wname}',{age},'{Address}',{Salary});")
#  conn.commit()
#  fet=conn.execute("SELECT * FROM COMPANY ORDER BY ID DESC LIMIT 1")
#  print(fet.fetchone())
# addNewWorker()

#in sqlite PRIMARY KEY("ID" AUTOINCREMENT)