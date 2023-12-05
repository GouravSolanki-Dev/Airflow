import random
import polars as pl
from datetime import datetime
import pyodbc

# Connect to the SSMS server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I8QHF1P\GOURAV;DATABASE=mitel;UID=sa;Pwd=123')


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
        new['Account NO']=n
        new['Transaction Type']=s
        new['Amount']=a
        for i in Balance:
            if i[0]==n:
                new['Balance']=i[1]
        new['Time']=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
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
    new={}
    new['Account NO']=random.randint(10**10, 10**11 - 1)
    new['Name']=''
    while new['Name'].strip() == '':
        new['Name'] = input('Enter Name:')
    #new['Name']=(input('Enter Name:'))

    new['DOB']=''
    while new['DOB'].strip() == '':
        new['DOB']=(input('Enter Date of Birth:'))

    new['Gender']=''
    while new['Gender'].strip()=='':    
        new['Gender']=input('Enter Gender:')

    new['Account_Type']=''
    print('Enter Account Type\n 1. Savings\n 2. Current\n 3. Joint')
    while new['Account_Type'].strip()=='': 
        a=int(input('Enter Account_Type:'))
        if a==1:
            new['Account_Type']='Savings'
        elif a==2:
            new['Account_Type']='Current'
        elif a==3:
            new['Account_Type']='Joint'
        else:
            print('Wrong input')
            new['Account_Type']=''

    new['Phone No']=''
    while new['Phone No'].strip()=='':
        new['Phone No']=((input('Enter Mobile NO:')))

    new['Email']=input('Enter Email:')
    new['Father\'s Name']=input('Enter Father\'s Name:')
    new['Address']=input('Enter Address:')
    Bank.append(new)
    return 0

def viewAccount(n):
    if len(Bank) ==0:
        print('-----------------------------------------------------------------------------------')
        print('No Data')
        print('-----------------------------------------------------------------------------------')
    else:
        for i in Bank:
            if int(i['Account NO'])==n:
                print('-----------------------------------------------------------------------------------')
                print(pl.DataFrame(i))
                print('-----------------------------------------------------------------------------------')
            else:
                print('Not Found')
        #print(student[n - 1])
    return 0

def viewArchieve(n):
    if len(Archieve) ==0:
        print('-----------------------------------------------------------------------------------')
        print('No Data')
        print('-----------------------------------------------------------------------------------')
    else:
        for i in Archieve:
            if int(i['Account NO'])==n:
                print('-----------------------------------------------------------------------------------')
                print(pl.DataFrame(i))
                print('-----------------------------------------------------------------------------------')
            else:
                print('Not Found')
        #print(student[n - 1])
    return 0

def updateAccount(n):
    if len(Bank) == 0:
        print('-----------------------------------------------------------------------------------')
        print('No Data')
        print('-----------------------------------------------------------------------------------')
    else:
        for i in Bank:
            if int(i['Account NO'])==n:
                print('-----------------------------------------------------------------------------------')
                print(pl.DataFrame(i))
                print('-----------------------------------------------------------------------------------')
                print('What do you want to update: \n 1. Name\n 2. Phone No\n 3. Address\n 4. Email')
                choice = int(input())
                if choice == 1:
                    i['Name']=''
                    while i['Name'].strip() == '':
                        i['Name'] = input('Enter Name:')
                elif choice == 2:
                    i['Phone No']=''
                    while i['Phone No'].strip()=='':
                        i['Phone No']=((input('Enter Mobile NO:')))
                elif choice == 3:
                    i['Address'] = input('Enter new Address:')
                elif choice == 4:
                    i['Address'] = input('Enter new Email:')
            else:
                print('No data exist with this Account Number.')
    print('-----------------------------------------------------------------------------------')
    return 0

def deleteData(n):
    if len(Bank) == 0:
        print('-----------------------------------------------------------------------------------')
        print('No Data')
        print('-----------------------------------------------------------------------------------')
    else:
        for i in Bank:
            if int(i['Account NO'])==n:
                new=Bank.pop(i)
                Archieve.append(new)
    return 0

def transaction(n):
    if len(Bank) == 0:
        print('-----------------------------------------------------------------------------------')
        print('No Data Found')
        print('-----------------------------------------------------------------------------------')
    else:
        new=[]
        for i in Bank:
            if int(i['Account NO'])==n:
                print('Select the transaction\n 1. Credit\n 2. Debit')
                a=int(input())
                if a==1:
                    if len(Balance)==0:
                        new.append(n)
                        amount=int(input('Enter the Amount to add: '))
                        new.append(amount)
                        Balance.append(new) 
                        print('New Balance :',new[1])
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
        if len(Bank) == 0:
            print('-----------------------------------------------------------------------------------')
            print('No Data')
            print('-----------------------------------------------------------------------------------')
        else:
            n = int(input('Enter the Account Number: '))
            updateAccount(n)
    elif a == 3:
        if len(Bank) == 0:
            print('-----------------------------------------------------------------------------------')
            print('No Data')
            print('-----------------------------------------------------------------------------------')
        else:
            print('View\n1. All Data\n2. One student')
            b=int(input())
            if b==1:
                print('-----------------------------------------------------------------------------------')
                print(pl.DataFrame(Bank))
                print('-----------------------------------------------------------------------------------')
            else:        
                n = int(input('Enter the Account Number:  '))
                viewAccount(n)
    elif a == 4:
        if len(Bank) == 0:
            print('-----------------------------------------------------------------------------------')
            print('No Data To Delete')
            print('-----------------------------------------------------------------------------------')
        else:
            n = int(input('Enter the Account Number: '))
            deleteData(n)
    elif a == 5:
        if len(Archieve) == 0:
            print('-----------------------------------------------------------------------------------')
            print('No Data')
            print('-----------------------------------------------------------------------------------')
        else:
            print('View\n1. All Data\n2. One Account')
            b=int(input())
            if b==1:
                print('-----------------------------------------------------------------------------------')
                print(pl.DataFrame(Archieve))
                print('-----------------------------------------------------------------------------------')
            else:        
                n = int(input('Enter the Account Number:  '))
                viewArchieve(n)
    elif a==6:
            n = int(input('Enter the Account Number:  '))
            transaction(n)

            user_input = input("Do you want to continue? (yes/no): ")
            if user_input.lower() in ["no", "n"]:
                print("Exiting...")
                break
    elif a==7:
        n = int(input('Enter the Account Number:  '))
        viewTransaction(n)

                
        





