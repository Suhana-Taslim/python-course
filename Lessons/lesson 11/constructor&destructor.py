class Student:
    def __init__(self):
        print('Student Created.')

    def __del__(self):
        print('Destructor called, Student deleted.')   

obj = Student()
del obj         