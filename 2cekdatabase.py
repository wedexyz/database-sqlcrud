import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="mydatabasensor")
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE sensor2 (nama VARCHAR(255), datasensor VARCHAR(255))")

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)