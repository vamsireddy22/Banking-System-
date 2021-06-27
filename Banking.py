import mysql.connector as mysql

db_connection = mysql.connect(host='localhost',username='root',passwd='',database='Banking_System')

def CreateAccount():

    print("Creating New User Account")
    accnum = int(input("Enter the Account number for your Account:"))
    name = str(input("Enter the Name of Account Holder:"))
    intialDeposit = int(input("Enter the Greater than 1000 Amount to open your Account:"))
    typeOfAccount = str(input("Choose either Savings/Current Account:"))
    phnum = int(input("Enter your Mobile Number:"))

    mycur = db_connection.cursor()

    # Inserting queries the data into the Account, Amount
    query = "insert into account values(%s,%s,%s,%s,%s)"
    query1 = "insert into amount values(%s,%s)"

    # Data to insert 
    data = (accnum,name,intialDeposit,typeOfAccount,phnum)
    data1 = (accnum,intialDeposit)

    # Executing the queries
    mycur.execute(query,data)
    mycur.execute(query1,data1)

    db_connection.commit()
    print("Successfully Created your Account")

def DepositAmount():

    print("Deposit Machine")
    accnum = int(input("Enter the Account Number to Deposit:"))
    amount = int(input("Enter money you wish to deposit:"))

    # Query
    query = "update account set amount=amount+{} where AccNum=accnum".format(amount)
    query1 = "update amount set amount=amount+{} where AccNum=accnum".format(amount)

    mycur = db_connection.cursor()

    mycur.execute(query)
    mycur.execute(query1)

    db_connection.commit()

    print("Deposit successfully in Account Number {}".format(accnum))

def WithDrawalAmount():

    print("With Drawal Machine")
    accnum = int(input("Enter the Account Number to Deposit :"))
    amount = int(input("Enter money you wish to withdrawal :"))

    mycur = db_connection.cursor()
    query = "select Amount from amount where AccNum={}".format(accnum)

    mycur.execute(query)
    availableBalance = mycur.fetchone()

    temp = availableBalance[0] - amount

    query1 = "update amount set Amount={} where AccNum={}".format(temp,accnum)
    query2 = "update account set Amount={} where AccNum={}".format(temp,accnum)
    mycur.execute(query1)
    mycur.execute(query2)
    db_connection.commit()

    print("Withdrawal Successfull")

    query = "select * from account where AccNum={}".format(accnum)
    mycur.execute(query)
    availableBalance = mycur.fetchone()
    print("Available Balance: ",availableBalance[2])

def BalanceEnquiry():

    print("Balance Enquiry Machine")
    accnum = int(input("Enter your account number : "))

    query = "select * from account where AccNum={}".format(accnum)

    mycur = db_connection.cursor()

    mycur.execute(query)

    availableBalance = mycur.fetchone()

    print("Available Balance: ",availableBalance[2])

    #db_connection.commit()

def DetailsOfUser():

    print("User Details")
    accnum = int(input("Enter your Account number : "))

    mycur = db_connection.cursor()

    query = "select * from account where AccNum={}".format(accnum)

    mycur.execute(query)
    print("Account Details")
    for i in mycur:
        print(i)

def DeleteUser():

    print("Deleting Your Account")
    accnum = int(input("Enter your account number: "))

    query = "delete from account where AccNum={}".format(accnum)
    query1 = "delete from amount where AccNum={}".format(accnum)

    mycur = db_connection.cursor()

    mycur.execute(query)
    mycur.execute(query1)

    db_connection.commit()

    print("{} Account removed from our bank".format(accnum))
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
        print("Thanks for using our bank")
        print("See You Again !")
        break



