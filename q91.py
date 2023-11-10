import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="DBADI")
mycur = mydb.cursor()

#Altering table
mycur.execute("ALTER TABLE customer ADD COLUMN id INT AUTO_INCREMENT=100 PRIMARY KEY")

