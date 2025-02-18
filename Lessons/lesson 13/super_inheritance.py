class Grand_Father:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Grand_son(Grand_Father):
    def __init__(self, fname, lname, age, salary):
        super().__init__(fname, lname)
        self.age = age
        self.salary = salary

x = Grand_son("Ahyan", "Shaik", 23, 30000)
x.printname()
print(x.age)
print(x.salary)