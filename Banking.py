import mysql.connector as mysql

db_connection = mysql.connect(host='localhost',username='root',passwd='',database='Banking_System')

mycursor = db_connection.cursor()

def CreateAccount():
    print("Creating New User Account")
    accnum = int(input("Enter the Account number for your Account:"))
    name = str(input("Enter the Name of Account Holder:"))
    intialDeposit = int(input("Enter the Greater than 1000 Amount to open your Account:"))
    typeOfAccount = str(input("Choose either Savings/Current Account:"))
    phnum = int(input("Enter your Mobile Number:"))


    
    print("Successfully Created your Account")

def DepositAmount():
    print("Deposit Machine")
    accnum = int(input("Enter the Account Number to Deposit:"))
    amount = int(input("Enter money you wish to deposit:"))




    print("Deposit successfully in Account Number {}".format(accnum))

def WithDrawalAmount():
    print("With Drawal Machine")
    accnum = int(input("Enter the Account Number to Deposit:"))
    amount = int(input("Enter money you wish to deposit:"))

    BalanceEnquiry()

def BalanceEnquiry():
    print("Balance Enquiry Machine")
    pass

def DetailsOfUser():
    print("User Details")
    pass

def DeleteUser():
    print("Deleting Your Account")
    accnum = int(input("Enter your account number: "))


    print("{} Account removed from our bank")
    print("Thanks for using, we are happy serve you")

while(True):

    print("Welcome to Python Banking System")
    print("1. Create New User")
    print("2. Deposit Amount")
    print("3. Withdrawal Amount")
    print("4. Balance Enquiry")
    print("5. Print details of User")
    print("6. Remove Account")
    print("7. Exit")

    option = int(input("Enter what would you like to do : "))

    if(option == 1):
        CreateAccount()
    elif(option == 2):
        DepositAmount()
    elif(option == 3):
        WithDrawalAmount()
    elif(option == 4):
        BalanceEnquiry()
    elif(option == 5):
        DetailsOfUser()
    elif(option == 6):
        DeleteUser()
    elif(option == 7):
        print("Thanks for using our bank.")
        print("See You Again !")
        break



