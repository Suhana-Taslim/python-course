set_1 = {2, 2, 4, 6, 6, 8, 8, 8, 3}
print("set:", set_1)

set_1.add(10)
print("Updated Set:", set_1)

set_2 = set_1
set_3 = {23, 14, 15, 15, 15, 18}

print("\nSet 1",set_2)
print("Set 2",set_3)
print("Difference")
print(set_2.difference(set_3))
print("Symmeteric Difference")
print(set_2.symmetric_difference(set_3))