import mysql.connector as mysql
from datetime import date


# replace passwd with your mysql workbench password
db_connection = mysql.connect(host='localhost',username='root',passwd='',database = 'library')


def addStudent():
    sid = int(input("Enter student ID : "))
    sname = input("Enter student name : ")
    branch = input("Enter student branch : ")
    year = input("Enter student year : ")
    mailid = input("Enter student mail id : ")

    cursor = db_connection.cursor()

    # Insert the data 
    query = "insert into student values(%s,%s,%s,%s,%s)"
    data = (sid,sname,branch,year,mailid)

    cursor.execute(query,data)
    db_connection.commit()

    print("Successfully added student into the database")

    menuOption = int(input("Press 1 to goback to main menu"))
    if(menuOption==1):
        return


def addBook():
    bid = int(input("Enter book ID : "))
    bname = input("Enter book name : ")
    author = input("Enter book author name : ")
    price = int(input("Enter the price of book : "))
    pages = int(input("Enter the no.of pages : "))
    status = input("Enter the status of book  avail/issued : ")
    copies = int(input("Enter the no.of copies : "))

    cursor = db_connection.cursor()

    #insert data into the books table

    query = "insert into books values(%s,%s,%s,%s,%s,%s)"
    data = (bid,bname,author,price,pages,status)

    for i in range(0,copies):
        cursor.execute(query,data)
    
    db_connection.commit()

    print("Successfully added books into the database")

    menuOption = int(input("Press 1 to goback to main menu"))
    if(menuOption==1):
        return

def checkBookStatus(bookId):

    query = 'select * from books where bid = '+bookId+';'
    
    cursor = db_connection.cursor()
    cursor.execute(query)

    result = cursor.fetchone()

    if(result[5]=="available"):
        return True
    else:
        return False

def issueBook():
    
    print("I am in Issue Counter")
    bid = input("Book Id : ")
    sid = int(input("Student ID : "))
    dat = date.today()

    # Error

    # status = checkBookStatus(bid)
    curs = db_connection.cursor()

    if(True):
        query = "insert into transactions values(%s,%s,%s)"
        data = (sid,bid,dat)

        curs.execute(query,data)

        query = 'update books set status = "issued" where bid = '+bid+''

        curs.execute(query)
        db_connection.commit()

        print("Suucessfully Issued Book")
    
    else:
        print("Book is not available")
        

def returnBook():
    pass

def modifyBook():
    pass

def issuedBooks():
    
    query = 'select * from books where status="issued";'

    cursor = db_connection.cursor()
    cursor.execute(query)

    results = cursor.fetchall()
    for record in results:
        print(record)

    db_connection.commit()

    menuOption = int(input("Press 1 to goback to main menu"))
    if(menuOption==1):
        return

def availableBooks():
    query = 'select * from books where status="available";'

    cursor = db_connection.cursor()
    cursor.execute(query)

    results = cursor.fetchall()
    for record in results:
        print(record)

    db_connection.commit()

    menuOption = int(input("Press 1 to goback to main menu"))
    if(menuOption==1):
        return




while(True):
    print("********** Main Menu ***********")
    print("1. Add Student")
    print("2. Add Books")
    print("3. Issue a book")
    print("4. Return a book")
    print("6. Modify Book Information")
    print("7. View issued books in library")
    print("8. View all available books in library")
    print("Type 0 to exit from application")
    
    choice = int(input("Enter your choice : ")) #7
    if(choice == 1):
        addStudent()
    elif(choice == 2):
        addBook()
    elif(choice == 3):
        issueBook()
    elif(choice == 4):
        returnBook()
    elif(choice == 5):
        searchBook()
    elif(choice == 6):
        modifyBook()
    elif(choice == 7):
        issuedBooks()
    elif(choice == 8):
        availableBooks()
    elif(choice == 0):
        break
    else:
        print("Invalid Selection")
