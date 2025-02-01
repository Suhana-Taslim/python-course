my_tuple = ()
print(my_tuple)

my_tuple = (10, 28, 34)
print(my_tuple)

my_tuple = (99,"Hello World!!", 3.4)
print(my_tuple)

my_tuple = ("Calender", [43, 24, 76], (6, 8, 10))
print(my_tuple)

my_tuple = ('g', 'e', 'r', 'm', 'a', 'n', 'y')
print(my_tuple[2])
print(my_tuple[6])

new_tuple = ("Calender", [43, 24, 76], (6, 8, 10))

print(new_tuple[0][5])
print(new_tuple[1][2])
print(new_tuple[2][1])

print("Sliced :", my_tuple[1:4])

for letter in(my_tuple):
    print("Hello!!", letter)