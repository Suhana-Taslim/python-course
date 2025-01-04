height=(float(input("enter the height")))
weight=(float(input("enter the weight")))

BMI=weight/((height/100)**2)
print("the BMI is",BMI)
if BMI<=18.4:
    print("you are under weight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=28.4:
    print("you are over weight")
elif BMI<=30.2:
    print("you are obese")
else:
    print("you are extremely over obese")