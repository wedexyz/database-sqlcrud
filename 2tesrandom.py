import random
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="1234",database="mydatabasensor")
mycursor = mydb.cursor()

while True :
    
    sql = "INSERT INTO sensor (nama, datasensor) VALUES (%s, %s)"
    val = [('datarandom', random.randint(0,100))]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")
    print(val)