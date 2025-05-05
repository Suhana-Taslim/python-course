import random 

print("Let's compare numbers")
print("Type 'greater, 'less' , 'equal")

score = 0

for i in range(3):
    a=random.randint(1 , 100)
    b=random.randint(1 , 100)

    print(f"\n which is true about {a} and {b}?")
    answer = input('your answer (greater / less / equal):').lower()

    if a > b and answer == "greater":
        print("Yes!! You're right")
        score += 1 
    elif a < b and answer == "less":
        print("Good Job that's correct")
        score += 1
    elif a == b and answer == "equal":
        print("Yayy!! You got it right")
        score += 1
    else:
        print("Oops!! Not quite...")
        if a > b:
            print(f"The right answer is : {a} is greater than {b}")
        elif a < b:
             print(f"The right answer is : {a} is less than {b}")
        else:
             print(f"The right answer is : {a} is equal to{b}")
print(f"\n All done you got {score} out of 3 correct!!")