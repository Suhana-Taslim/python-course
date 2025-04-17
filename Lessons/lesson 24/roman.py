def roman_to_int(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':10000}
    total = 0
    prev = 0
    for ch in reversed(s):
        val = roman[ch]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

roman = input("Enter a roman numeral (like XIV): ").ipper()
print(f"The number is : {roman_to_int(roman)}")