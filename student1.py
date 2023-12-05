student = []

def createStudent():
    # student.append([])
    nested_student = []
    # student[len(student)-1].append(len(student)-1)
    nested_student.append(input('Enter Roll no: '))
    print('Enter Name:')
    # student[len(student) - 1].append(input())
    nested_student.append(input())
    print('Enter Age:')
    # student[len(student) - 1].append(int(input()))
    nested_student.append(input())
    print('Enter Address:')
    # student[len(student) - 1].append(input())
    nested_student.append(input())
    student.append(nested_student)
    return 0

def viewStudent(n):
    if len(student) == 0 or n > len(student) or n <= 0:
        print('Invalid student roll number.')
    else:
        for i in student:
            if i[0]==n:
                print('_______________________________________________________')
                print(' | '+i[0]+' | '+i[1]+' | '+i[2]+' | '+i[3]+' | ')
            else:
                print('No input found')
    return 0

def updateStudent(n):
    if len(student) == 0 or n > len(student) or n <= 0:
        print('Invalid student roll number.')
    else:
        print(student[n])
        print('What value you want to update: \n 1. Name\n 2. Age\n 3. Address')
        choice = int(input())
        if choice == 1:
            student[n][1] = input('Enter new Name:')
        elif choice == 2:
            student[n][2] = int(input('Enter new Age:'))
        elif choice == 3:
            student[n][3] = input('Enter new Address:')
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
        print('1. All Data \n2. One student data')
        b=input()
        if b==1:
            print('_______________________________________________________')
            for i in student:
                print(' | '+i[0]+' | '+i[1]+' | '+i[2]+' | '+i[3]+' | ')
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
