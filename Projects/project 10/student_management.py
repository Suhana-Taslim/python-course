print("Student Details\n")

print("Enter 1 to enter student details\n Enter 2 to exit")


choice = (int (input('Enter ur choice:')))
if choice==1:
    print("Enter the details")
    name = (str (input("Enter Student Name:")))
    age = (int (input("Enter Students Age:")))
    roll_no = (int (input("Enter Students Roll No:")))
    grade = (int (input("Enter The Grade:")))

    print("The Student Name is:-",name)
    print("The Age of Student is:-",age)
    print("The Roll no of Student is:-",roll_no)
    print("The Grade of Student is:-",grade)

elif choice==2:
    print("Student profile exited")

else:
    print("Wrong number entered")