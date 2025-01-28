list = ['pink', 'orange', 'yellow', 'white', 'black', 'green']

print("Length of list:" ,len(list))
print("First element:" ,list[0])
print("Last element:" ,list[-1])

list.append('blue')
print("Updated list:", list)

list.remove('pink')
print("Updated list:", list)

list.sort()
print("Sorted list:", list)

list.pop(1)
print("updated list :",list)

list.reverse()
print("Reversed list:", list)

print("Multiplication on list :",list*2)

list = list[:4]
print("Sliced list :", list)

list.clear()
print("Updated list :", list)