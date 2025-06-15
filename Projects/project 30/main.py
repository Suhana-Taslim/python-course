print("Welcome to the power set maker quiz")

input_string = input("Enter 3 numbers seperated by commas (like 1,2,3) : ")

items = input_string.split(",")

items = [item.strip() for item in items]

power_set = [[]]

for item in items:
    print(f"\n adding item: {item}")
    new_subsets = []
    
    for subset in power_set:
        new_subset = subset + [item]
        print(f" ➕ adding {item} to {subset} -> {new_subset}")
        new_subsets.append(new_subset)

    power_set.extend(new_subsets)

print("\n final power set:")
for subset in power_set:
    print(subset)

print("\n YAY!! you made a power set")