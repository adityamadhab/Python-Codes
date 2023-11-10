import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="")
mycur = mydb.cursor()
#Create Database
mycur.execute("CREATE DATABASE DBADI")
#Show database
mycur.execute("SHOW DATABASES")
for x in mycur:
    print(x)


