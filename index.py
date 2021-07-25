import mysql.connector as mysql

db_connection = mysql.connect(host='localhost',username='root',passwd='',database = 'library')


def addStudent():
    sid = int(input("Enter student ID : "))
    sname = input("Enter student name : ")
    branch = input("Enter student branch : ")
    year = input("Enter student year : ")
    mailid = input("Enter student mail id : ")

    pass

def addBook():
    bid = int(input("Enter book ID : "))
    bname = input("Enter book name : ")
    author = input("Enter book author name : ")
    price = int(input("Enter the price of book : "))
    pages = int(input("Enter the no.of pages : "))
    status = input("Enter the status of book  avail/issued : ")
    copies = int(input("Enter the no.of copies : "))

    pass

def issueBook():
    pass

def returnBook():
    pass

def searchBook():
    pass

def modifyBook():
    pass




while(True):
    print("1. Add Student")
    print("2. Add Books")
    print("3. Issue a book")
    print("4. Return a book")
    print("5. Book search")
    print("6. Modify Book Information")
    print("Type 0 to exit from application")
    
    choice = int(input("Enter your choice : "))
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
    elif(choice == 0):
        break
    else:
        print("Invalid Selection")
    

