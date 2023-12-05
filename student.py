student=[[]]

#------------------------------------------------------------------------------------------------------
def createStudent():
    a=len(student)
    student[len(student)].append(a+1)
    print('Enter Name: ')
    student[len(student)-1].append(input())
    print('Enter Age: ')
    student[len(student)-1].append(input())
    print('Enter Address')
    student[len(student)-1].append(input())
    return 0

#------------------------------------------------------------------------------------------------------

def viewStudent(n):
    if len(student)<1:
        return('No values to See.')
    else:
        print(student[n-1])
        return 0

#------------------------------------------------------------------------------------------------------

def updateStudent(student,n):
    if (len(student)==0):
        print('No values to update.')
    else:
        print('What value you want to append: \n 1. Name\n 2. Age\n 3. Student')
        a=int(input())
        if a==1:
            student[n-1][1]=input()
        elif a==2:
            student[n-1][2]=int(input())
        elif a==3:
            student[n-1][3]=input()
    return 0

#-----------------------------------------------------------------------------------------------------

def deleteData(n):
    if len(student)==0:
        return('No values to delete.')
    else:
        student.pop(n-1)
    return 0


#=====================================================================================================
while True:
    print('========================================Menu=========================================')
    print('     1. Create\n     2. Update\n     3. View\n       4. Delete')
    a=int(input())
    if a==1:
        createStudent()
    if a==2:
        n=int(input('What is the roll no of student: '))
        updateStudent(student,n)
    if a==3:
        n=int(input('What is the roll no of student: '))
        viewStudent(n)
    if a==4:
        n=int(input('What is the roll no of student: '))
        deleteData(n)

    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() in ["no", "n"]:
        print("Exiting...")
        break
    else:
        print("Invalid input. Please enter yes/no.")


