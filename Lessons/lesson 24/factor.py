print("🎉Welcome to the factor finder!")
print("Give me any number, and I'll show you all its factors!!")

num = int(input("🔢Enter a number: "))

print(f"\n 🔍 Finding factors of {num}...")

for i in range(1, num + 1):
    if num % i == 0:
        print(f"✅ {i} is a factor of {num}")

print("\n 🎉🎉All Done That was Fun!!")