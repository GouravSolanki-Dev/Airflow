student = []

def createStudent():
    new=[]
    new.append(input('Enter Roll no:'))
    new.append(input('Enter Name:'))
    new.append(int(input('Enter Age:')))
    new.append(input('Enter Address:'))
    student.append(new)
    return 0

def viewStudent(n):
    if len(student) < 1 or n > len(student) or n <= 0:
        print('Invalid student roll number.')
    else:
        for i in student:
            if int(i[0])==n:
                print('-----------------------------------------------------------------------------------')
                print('| '+f'{i[0]:<5}'+' | '+f'{i[1]:<30}' +' | '+f'{str(i[2]):<5}'+' | '+f'{i[3]:<30}'+' |')
                print('-----------------------------------------------------------------------------------')
            else:
                print('Not Found')
        #print(student[n - 1])
    return 0

def updateStudent(n):
    if len(student) == 0 or n > len(student) or n <= 0:
        print('Invalid student roll number.')
    else:
        for i in student:
            if int(i[0])==n:
                print('-----------------------------------------------------------------------------------')
                print('| '+f'{i[0]:<5}'+' | '+f'{i[1]:<30}' +' | '+f'{str(i[2]):<5}'+' | '+f'{i[3]:<30}'+' |')
                print('-----------------------------------------------------------------------------------')
                print('What value you want to update: \n 1. Name\n 2. Age\n 3. Address')
                choice = int(input())
                if choice == 1:
                    student[n - 1][1] = input('Enter new Name:')
                elif choice == 2:
                    student[n - 1][2] = int(input('Enter new Age:'))
                elif choice == 3:
                    student[n - 1][3] = input('Enter new Address:')
    return 0

def deleteData(n):
    if len(student) == 0 or n > len(student) or n <= 0:
        print('Invalid student roll number.')
    else:
        student.pop(n - 1)
    return 0

while True:
    print('========================================Menu=========================================')
    print('     1. Create\n     2. Update\n     3. View\n     4. Delete')
    a = int(input())
    if a == 1:
        createStudent()
    if a == 2:
        n = int(input('Enter the roll no of the student: '))
        updateStudent(n)
    if a == 3:
        print('View\n1. All Data\n2. One student')
        b=int(input())
        if b==1:
            print('-----------------------------------------------------------------------------------')
            for i in student:
                #print('| '+i[0]+' | '+i[1]+' | '+str(i[2])+' | '+i[3]+' |')
                print('| '+f'{i[0]:<5}'+' | '+f'{i[1]:<30}' +' | '+f'{str(i[2]):<5}'+' | '+f'{i[3]:<30}'+' |')
                print('-----------------------------------------------------------------------------------')
        else:        
            n = int(input('Enter the roll no of the student: '))
            viewStudent(n)
    if a == 4:
        n = int(input('Enter the roll no of the student: '))
        deleteData(n)

    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() in ["no", "n"]:
        print("Exiting...")
        break
