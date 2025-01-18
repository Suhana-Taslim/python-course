def recur_factorial(n) :
    if n==1:
        return n 
    else:
        return n*recur_factorial(n-1)
    
num = int(input("Enter a Number"))

if num<0:
        print("The given number is less than 0")
elif num==0:
        print("the given number is Zero")
else:
        print("The Factorial of",num,"is",recur_factorial(num))