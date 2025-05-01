def check_bit():
    print("Welcome to the bit checker game!")
    print("you will enter a number, and I'll tell you whether its a 0-bit or a 1-bit.\n")

    while True:
        bit = input("Enter a bit(0/1) or type 'exit' to quit:").strip()

        if bit.lower() == 'exit':
            print("Thanks for playing byee!")
            break
        elif bit == '0':
            print("you entered 0 Thats a one bit\n")
        elif bit == 1:
            print("you entered 1Thats a one bit\n")
        else:
            print("Oops!! Thats not a valid bit. Please enter only 0 or 1.\n")

check_bit()