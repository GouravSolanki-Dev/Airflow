import random
import polars as pl
from datetime import datetime
import pyodbc

# Connect to the SSMS server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I8QHF1P\GOURAV;DATABASE=ATM_Console;UID=sa;Pwd=123')
# Create a cursor object
cursor = conn.cursor()

Bank = []
Archieve=[]
Balance=[]
Cred=[["Admin",'A@123'],['GSR','A@123']]
Transactions=[]

def newTransaction(n,s,a):
    new={}
    if len(Balance)==0:
        print('No transaction till now.')
    else:
        Account_NO=n
        #Transaction Type=s
       ##Time']=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    Transactions.append(new)


def viewTransaction(n):
    if len(Transactions) ==0:
        print('-----------------------------------------------------------------------------------')
        print('No Data')
        print('-----------------------------------------------------------------------------------')
    else:
        for i in Transactions:
            if int(i['Account NO'])==n:
                print('-----------------------------------------------------------------------------------')
                print(pl.DataFrame(i))
                print('-----------------------------------------------------------------------------------')
            else:
                print('Not Found')
        #print(student[n - 1])
    return 0


def createAccount():
    Name=''
    while Name.strip() == '':
        Name = input('Enter Name:')
    #Name']=(input('Enter Name:'))

    DOB=''
    while DOB.strip() == '':
        DOB=(input('Enter Date of Birth(dd-mm-yyyy):'))
        #formatted_dob = datetime.datetime.strftime(DOB, '%Y-%m-%d') if isinstance(DOB, datetime.datetime) else DOB
        

    Gender=''
    while Gender.strip()=='':    
        Gender=input('Enter Gender:')

    Account_Type=''
    print('Enter Account Type\n 1. Savings\n 2. Current\n 3. Joint')
    while Account_Type.strip()=='': 
        a=int(input('Enter Account_Type:'))
        if a==1:
            Account_Type='Savings'
        elif a==2:
            Account_Type='Current'
        elif a==3:
            Account_Type='Joint'
        else:
            print('Wrong input')
            Account_Type=''

    Phone_No=''
    while Phone_No.strip()=='':
        Phone_No=((input('Enter Mobile NO:')))

    Email=input('Enter Email:')
    Fathers_Name=input('Enter Father\'s Name:')
    Address=input('Enter Address:')
    # Execute a SQL query
    #cursor.execute(f'insert into Account values(FLOOR(RAND(CHECKSUM(NEWID()))*(99999999999-10000000000)+10000000000),{Name},{DOB},{Gender},{Account_Type},{Phone_No},{Email},{Fathers_Name},{Address}')
    cursor.execute(f"INSERT INTO Account (Account_no, [Name], Dob, Gender, Account_Type, Phone_No, Email, [Fathers_name], [Address]) VALUES "
               f"(FLOOR(RAND(CHECKSUM(NEWID()))*(99999999999-10000000000)+10000000000), "
               f"'{Name}', "
               f"'{DOB}', "  # Assuming DOB is a string in 'YYYY-MM-DD' format
               f"'{Gender}', "
               f"'{Account_Type}', "
               f"{Phone_No}, "
               f"'{Email}', "
               f"'{Fathers_Name}', "
               f"'{Address}')")
    cursor.commit()
    return 0


def viewAccount(n):
    # Assuming cursor is already created and connected to the database

    # Check if there is any data in the 'account' table
    cursor.execute('SELECT COUNT(*) FROM account')
    count_result = cursor.fetchone()

    if count_result == 0:
        print('-----------------------------------------------------------------------------------')
        print('No Data')
        print('-----------------------------------------------------------------------------------')
    else:
        # Retrieve the details for the specific account number 'n'
        cursor.execute(f"SELECT * FROM account WHERE account_no = {n}")
        account_data = cursor.fetchone()

        if account_data:
            print('-----------------------------------------------------------------------------------')
            print('Account Details')
            print('-----------------------------------------------------------------------------------')
            print(f"Account Number: {account_data.Account_no}")
            print(f"Name: {account_data.Name}")
            print(f"DOB: {account_data.Dob}")
            print(f"Gender: {account_data.Gender}")
            print(f"Account Type: {account_data.Account_Type}")
            print(f"Phone Number: {account_data.Phone_No}")
            print(f"Email: {account_data.Email}")
            print(f"Father's Name: {account_data.Fathers_name}")
            print(f"Address: {account_data.Address}")
            print('-----------------------------------------------------------------------------------')
        else:
            print('-----------------------------------------------------------------------------------')
            print(f'No data found for account number {n}')
            print('-----------------------------------------------------------------------------------')


def viewArchieve(n):
    cursor.execute('SELECT COUNT(*) FROM archieve')
    count_result = cursor.fetchone()

    if count_result == 0:
        print('-----------------------------------------------------------------------------------')
        print('No Data')
        print('-----------------------------------------------------------------------------------')
    else:
        cursor.execute(f"SELECT * FROM archieve WHERE account_no = {n}")
        account_data = cursor.fetchone()
        cursor.commit()

        if account_data:
            print('-----------------------------------------------------------------------------------')
            print('Account Details')
            print('-----------------------------------------------------------------------------------')
            print(f"Account Number: {account_data.Account_no}")
            print(f"Name: {account_data.Name}")
            print(f"DOB: {account_data.Dob}")
            print(f"Gender: {account_data.Gender}")
            print(f"Account Type: {account_data.Account_Type}")
            print(f"Phone Number: {account_data.Phone_No}")
            print(f"Email: {account_data.Email}")
            print(f"Father's Name: {account_data.Fathers_name}")
            print(f"Address: {account_data.Address}")
            print('-----------------------------------------------------------------------------------')
        else:
            print('-----------------------------------------------------------------------------------')
            print(f'No data found for account number {n}')
            print('-----------------------------------------------------------------------------------')
    return 0

def updateAccount(n):
    cursor.execute('SELECT COUNT(*) FROM account')
    count_result = cursor.fetchone()

    if count_result == 0:
        print('-----------------------------------------------------------------------------------')
        print('No Data')
        print('-----------------------------------------------------------------------------------')
    else:
        print('What do you want to update: \n 1. Name\n 2. Phone No\n 3. Address\n 4. Email')
        choice = int(input())
        if choice == 1:
            name=''
            while name.strip() == '':
                name = input('Enter Name:')
            cursor.execute(f"update Account set [Name]='{name}' where account_no={n}")
        elif choice == 2:
            Phone_no=''
            while Phone_no.strip()=='':
                Phone_no=((input('Enter Mobile NO:')))
            cursor.execute(f"update Account set [Phone_no]='{Phone_no}' where account_no={n}")
        elif choice == 3:
            Addres = input('Enter new Address:')
            cursor.execute(f"update Account set [Address]='{Addres}' where account_no={n}")

        elif choice == 4:
            email = input('Enter new Email:')
            cursor.execute(f"update Account set [Email]='{email}' where account_no={n}")

            # else:
            #     print('No data exist with this Account Number.')
        cursor.commit()
    print('-----------------------------------------------------------------------------------')
    return 0

def deleteData(n):
    cursor.execute('SELECT COUNT(*) FROM account')
    count_result = cursor.fetchone()

    if count_result == 0:
        print('-----------------------------------------------------------------------------------')
        print('No Data')
        print('-----------------------------------------------------------------------------------')
    else:
        cursor.execute(f"insert into archieve select * from account where account_no = {n}")
        cursor.execute(f"delete from account where account_no = {n}")
        cursor.commit()
    return 0

def transaction(n):
    cursor.execute('SELECT COUNT(*) FROM Balance')
    count_result = cursor.fetchone()

    if count_result == 0:
        print('-----------------------------------------------------------------------------------')
        print('No Data')
        print('-----------------------------------------------------------------------------------')
    else:
        print('Select the transaction\n 1. Credit\n 2. Debit')
        a=int(input())
        if a==1:
            cursor.execute(f'SELECT Balance_amount FROM Balance where account_no = {n}')
            balance = cursor.fetchone()
            if balance[0]==0:
                amount=int(input('Enter the Amount to add: '))
                cursor.execute(f"update Balance set Balance_amount={amount} where account_no = {n}")
                cursor.commit()
                # new.append(n)
                # amount=int(input('Enter the Amount to add: '))
                # new.append(amount)
                # Balance.append(new) 
                # print('New Balance :',new[1])
                newTransaction(n,'Credit',amount) 
            else:
                for j in Balance:
                    if j[0]==n:
                        if j[1]>=0:
                            amount=int(input('Enter the Amount to add: '))
                            j[1]+=amount
                            print(f'New Balance :',j[1]) 
                            newTransaction(n,'Credit',amount) 
                        else:
                            amount=int(input('Enter the Amount to add: '))
                            j[1]=amount  
                            print(f'New Balance :',j[1])
                            newTransaction(n,'Credit',amount) 
        elif a==2:
            if len(Balance)==0:
                print('No data Found')
            else:
                for j in Balance:
                    if j[0]==n:
                        if j[1]<=0:
                            print('No amount to debit') 
                        else:
                            b=int(input('Enter the Amount to Debit: '))
                            if j[1]-b<0:
                                print('Invalid amount to debit, select less amount')
                            else:
                                j[1]=j[1]-b
                                print('New Balance is :', j[1])
                                newTransaction(n,'Debit',b)

                    



         

while True:
    print('========================================Menu=========================================')
    print('     1. Create\n     2. Update\n     3. View\n     4. Delete\n     5. Archieve\n     6. Transaction\n     7. View Transaction')
    print('=====================================================================================')
    a = int(input())
    if a == 1:
        createAccount()
    elif a == 2:
        n = int(input('Enter the Account Number: '))
        updateAccount(n)
    elif a == 3:
        print('1. All Data\n2. One Account')
        acc=int(input())
        if acc==1:
            cursor.execute(f"SELECT * FROM account")
            account_data = cursor.fetchall()
            if account_data:
                print('-----------------------------------------------------------------------------------')
                print('Account Details')
                print('-----------------------------------------------------------------------------------')
                for i in account_data:
                    print(f"Account Number: {i.Account_no}")
                    print(f"Name: {i.Name}")
                    print(f"DOB: {i.Dob}")
                    print(f"Gender: {i.Gender}")
                    print(f"Account Type: {i.Account_Type}")
                    print(f"Phone Number: {i.Phone_No}")
                    print(f"Email: {i.Email}")
                    print(f"Father's Name: {i.Fathers_name}")
                    print(f"Address: {i.Address}")
                    print('-----------------------------------------------------------------------------------')
        else:
            n = int(input('Enter the Account Number:  '))
            viewAccount(n)
    elif a == 4:       
            n = int(input('Enter the Account Number: '))
            deleteData(n)
    elif a == 5:
            print('Archieve')
            n = int(input('Enter the Account Number:  '))
            viewArchieve(n)
    elif a==6:
            n = int(input('Enter the Account Number:  '))
            transaction(n)

            
    elif a==7:
        n = int(input('Enter the Account Number:  '))
        viewTransaction(n)

    else:
        user_input = input("Do you want to continue? (yes/no): ")
        if user_input.lower() in ["no", "n"]:
            print("Exiting...")
            # Close the cursor and connection
            cursor.close()
            conn.close()
            break
                
        





