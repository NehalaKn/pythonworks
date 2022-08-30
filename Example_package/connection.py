import pymysql
dbcon=pymysql.connect(host='localhost',user='root',password='NehalaKn@mysql90',database='nehala')
cobj=dbcon.cursor()

id1=int(input("Enter the Id:"))
add=input("Enter the address:")
ph=input("Enter the phone no:")
sql="insert into details values(%s,%s,%s)"
val=(id1,add,ph)

cobj.execute(sql,val)
dbcon.commit()
print("Inserted")