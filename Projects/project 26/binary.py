def binary_to_decimal(binary_str):
    try:
       
        decimal_number = int(binary_str, 2)
        print(f"The decimal equivalent of binary {binary_str} is {decimal_number}.")
    except ValueError:
        print("Invalid binary number. Please enter a string containing only 0s and 1s.")

binary_input = input("Enter a binary number: ")
binary_to_decimal(binary_input)
