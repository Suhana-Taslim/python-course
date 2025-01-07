print("Enter Details of the Canditate\n")
age=(int(input("Enter the canditate age:")))
height=(float(input("enter the candiate height in cm:")))
weight=(float(input("enter the weight of candiatate:")))
BMI=(float(input("enter the bmi:")))
if age>=18:
    if BMI>18:
        if BMI<26:
            print("Canditate is eligible")
        else :
            print("Canditate is not eligible")
    else :
        print("Canditate is not eligible")
else:
    print("Canditate is not eligible:")