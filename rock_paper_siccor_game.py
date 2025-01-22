import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    messagebox.showinfo("Result", f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n\n{result}")
    
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    score_label.config(text=f"Scores - You: {user_score}, Computer: {computer_score}")

def on_rock():
    play_game('rock')

def on_paper():
    play_game('paper')

def on_scissors():
    play_game('scissors')

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

rock_button = tk.Button(root, text="Rock", command=on_rock, width=20)
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=on_paper, width=20)
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=on_scissors, width=20)
scissors_button.pack(pady=10)

score_label = tk.Label(root, text=f"Scores - You: {user_score}, Computer: {computer_score}", font=("Helvetica", 14))
score_label.pack(pady=20)

root.mainloop()
