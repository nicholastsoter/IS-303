#Nick Soter
#Rock Paper Scissors Game

import random

#Grab user choice, convert it to lowercase and return it
def get_player_choice():
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    while player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
        player_choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()
    return player_choice

#Decide if the player wins, then return if they won, tied, or lost.
def determine_winner(player_choice):
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = "rock"
    elif computer_choice == 2:
        computer_choice = "paper"
    elif computer_choice == 3:
        computer_choice = "scissors"

    print(f"The computer chose {computer_choice}")
    if computer_choice == player_choice:
        print("Tie! Play Again.")
        return "tie"
    elif (computer_choice == "rock" and player_choice == "paper") or (computer_choice == "scissors" and player_choice == "rock") or (computer_choice == "paper" and player_choice == "scissors"):
        print("You won!")
        return "win"
    elif (computer_choice == "paper" and player_choice == "rock") or (computer_choice == "rock" and player_choice == "scissors") or (computer_choice == "scissors" and player_choice == "paper"):
        print("You lost!")
        return "loss"
    
#Actual beginning of the program
print("Welcome to Rock, Paper, Scissors!")

#Even and odd checking
total_rounds = int(input("How many rounds would you like to play: "))
while total_rounds % 2 == 0:
    print("Please enter an odd number to ensure a winner.")
    total_rounds = int(input("How many rounds would you like to play: "))

#Determine wins and losses
wins = 0
losses = 0
rounds_played = 0

while total_rounds > rounds_played:
    player_choice = get_player_choice()
    result = determine_winner(player_choice)
    if result == "win":
        wins += 1
        rounds_played += 1
    elif result == "loss":
        losses += 1
        rounds_played += 1

#Print Results
print("-------------------------")
print(f"Score -- You: {wins} | Computer: {losses}")
if wins > losses:
    print("You beat the computer!")
elif losses > wins:
    print("You lost to the computer!")
print("Thanks for playing!")








