import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")

choices = ["Rock", "Paper", "Scissors"]

def determine_winner(user_choice):
    computer_choice = random.choice(choices)
    result_text = f"Computer chose {computer_choice}.\n"
    
    if user_choice == computer_choice:
        result_text += "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_text += "You win!"
    else:
        result_text += "You lose!"
    
    result_label.config(text=result_text)

def reset_game():
    result_label.config(text="")

tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

for choice in choices:
    tk.Button(button_frame, text=choice, width=10, font=("Arial", 12),
              command=lambda c=choice: determine_winner(c)).pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 14), pady=20)
result_label.pack()

tk.Button(root, text="Reset Game", width=12, font=("Arial", 12), command=reset_game).pack(pady=10)

root.mainloop()
