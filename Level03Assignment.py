# Nick Soter
# Higher or Lower Game
import random

#Generate number
game_num = random.randint(1, 100)


#Welcome statements
print("--------------Higher or Lower----------------\n")
print("Welcome to Higher or Lower where the goal is to guess the number between 1 and 100.")
print("Try to guess in as few attempts as possible.\nGood luck!\n")

play_again = "y"

while play_again == "y" or play_again == "Y":
    #Variable assignments
    total_guesses = 1
    guess_num = 101

    #Game logic loop
    while game_num != guess_num:
        guess_num = int(input("Please enter your guess: "))
        if guess_num <= 0 or guess_num >= 101:
            print("Please enter a number between 1 and 100.\n")
        else:
            if guess_num < game_num:
                print("Your guess is too low!\n")
                total_guesses += 1
            if guess_num > game_num:
                print("Your guess is too high!\n")
                total_guesses += 1
    
    #Finish message logic (plus an extra message for the first try)
    if total_guesses == 1:
        finish_message = "First try!"
    elif total_guesses == 2 or total_guesses == 3:
        finish_message = "Amazing!"
    elif total_guesses <= 5:
        finish_message = "Impressive!"
    elif total_guesses <= 7:
        finish_message = "Good job!"
    elif total_guesses <= 9:
        finish_message = "Took a little longer but you go there!"
    elif total_guesses >= 10:
        finish_message = "You need to lock in."

    #Grammar handling
    if total_guesses == 1:
        print(f"{finish_message} You guessed the number {game_num} in {total_guesses} attempt.")
    elif total_guesses > 1:
        print(f"{finish_message} You guessed the number {game_num} in {total_guesses} attempts.")
    
    #Game reset logic
    play_again = input("Play again? (y/n): ")
    if play_again != "y" or play_again != "Y":
        print("Thank you for playing higher or lower!")
    elif play_again == "y" or play_again == "Y":
        game_num = random.randint(1, 100)
    