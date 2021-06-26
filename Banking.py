import mysql.connector as mysql

db_connection = mysql.connect(host='localhost',username='root',passwd='',database='Banking_System')

mycursor = db_connection.cursor()

#mycursor.execute("create database Banking_System")
mycursor.execute("create table Account(AccNum Integer,AccHolderName varchar(20),Amount integer,TypeOfAcc varchar(20), phno integer)")
mycursor.execute("create table Amount(AccNum integer, Amount Integer)")

print("Table created Successfully")



