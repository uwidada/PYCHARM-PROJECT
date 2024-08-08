import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="",database="hms")

mycursor = db.cursor()

mycursor.execute("SELECT * from doctors")
result = mycursor.fetchall()

for i in result:
   print(i)








