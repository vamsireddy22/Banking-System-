import mysql.connector as mysql

db_connection = mysql.connect(host='localhost',username='root',passwd='')

if(db_connection.is_connected()):
    print("Connection Successfull")
else:
    print("Connection Failed")