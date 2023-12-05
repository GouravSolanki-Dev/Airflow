import random
import polars as pl

Bank = []
Archieve=[]
Balance=[]
Cred=[["Admin",'A@123'],['GSR','A@123']]

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
    while new['Account_Type'].strip()=='': 
        new['Account_Type']=input('Enter Account_Type:')

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
                        new.append(int(input('Enter the Amount to add: ')))
                        Balance.append(new) 
                        print('New Balance :',new[1]) 
                    else:
                        for j in Balance:
                            if j[0]==n:
                                if j[1]>=0:
                                    j[1]+=int(input('Enter the Amount to add: '))
                                    print(f'New Balance :',j[1]) 
                                else:
                                    j[1]=int(input('Enter the Amount to add: '))  
                                    print(f'New Balance :',j[1])
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
                    



         

z=1
while z<=1:
    name1=input('Enter Username: ')
    pass1=input('Enter Password: ')
    for i in Cred:
        if i[0]==name1 and i[1]==pass1:
            print('========================================Menu=========================================')
            print('     1. Create\n     2. Update\n     3. View\n     4. Delete\n     5. Archieve\n     6. Transaction')
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
                    print('View\n1. All Data\n2. One student')
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
                
        else:
            print('Enter correct User Name/Password')
            z+=1
            break





