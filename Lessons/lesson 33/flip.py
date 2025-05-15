print("welcome to the flip bits fun show!!")

n = int(input("\n How many numbeers do you want to try?? "))

for i in range(n):
    print("\n Try {i+1}: ")
    user_number = int(input("enter any number:"))

    binary = bin(user_number)[2:]
    print(f"Binary of {user_number} is :{binary}")

    flipped = ""
    for bit in binary:
        if bit == '1':
            flipped += '0'
        else:
            flipped += '1'

    flipped_number = int(flipped, 2)

    print(f"Flipped binary is: {flipped}")
    print(f"Flipped number is: {flipped_number}")

print("\n that was fun !! you flipped some cool bits today")