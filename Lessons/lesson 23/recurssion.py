def reverse_word(word):
    if len(word) == 0:
        return ""
    return word[-1] + reverse_word(word[:-1])

print("Welcome to the Reverse it Game!!")
print("Type a word and I'll reverse it using recursion.")
print("Type 'exit' to stop.\n")

while True:
    user_word = input("Enter a Word:")
    if user_word.lower() == 'exit':
        break
    reversed_word = reverse_word(user_word)
    print(f"Reversed (Recursively): {reversed_word}")