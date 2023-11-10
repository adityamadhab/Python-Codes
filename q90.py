import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="",database="DBADI")
mycur = mydb.cursor()


#mycur.execute("CREATE TABLE customer(name varchar(250),address varchar(300),phone_no int(12))")

mycur.execute("SHOW TABLES")
for x in mycur :
    print(x)




