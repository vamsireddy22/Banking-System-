# Banking-System-

### Install Mysql [Link](https://dev.mysql.com/downloads/installer/)
### Install Pip [Link](https://bootstrap.pypa.io/get-pip.py)
- Open the above link and copy the contents present in it. 
- Go to code editor or notepad, paste it and save the file. 
- Open cmd and go to the folder where you have saved your file. 
- Now, enter the command py filename.py

### Creating the Banking Database Manual
- Open your Mysql Workbench and login to your localhost
- Copy the below commands in your workspace and execute one by one
- `create database bankingsystem`
- `use bankingsystem`
- `create table Account(AccNum Integer,AccHolderName varchar(20),Amount integer,TypeOfAcc varchar(20), phno integer)`
- `create table Amount(AccNum integer, Amount Integer)`
- Done! You have created database structure for your banking system

### Run the Project
- Open Banking.py file and copy the contents 
- Change the login credentials according to your's
- Change the database name to `bankingsystem`
- Done! Now you can execute the file. 
- Use command `py filename.py` in your command prompt
