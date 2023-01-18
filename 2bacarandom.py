import random
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="mydatabasensor")
mycursor = mydb.cursor()
while True :
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sensor")
    myresult = mycursor.fetchall()
    print(myresult)
