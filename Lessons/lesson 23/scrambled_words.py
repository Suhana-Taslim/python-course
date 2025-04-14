import random

words = ["apple", "banana", "mango", "grape", "orange", "melon", "berrries"]
word = random.choice(words)
scrambled = ' '.join(random.sample(word, len(word)))

print("🔠 Welcome to Word Scramble~")
print(f"Can you guess the word? \n Scrambled word : {scrambled}")

for attempt in range(3):
    guess = input(f"Attempt {attempt + 1}: ").lower()
    if guess == word:
        print("Correct You Guessed the word🎉!! ")
        break
    else:
        print("❌Try Again")
else:
    print(f"Out of Tries... The word was '{word}'.")