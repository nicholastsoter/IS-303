from wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won

# print(wordle) for debugging
# initialize variables
guess = ""
play_again = "Y"

#Game loop
while play_again == "Y":
    wordle = choose_word()
    #Initial Statements
    print("Welcome to mystery Wordle! \nGuess the 5 letter word.")
    print("\nG = correct letter and position\nY = correct letter, wrong position\n- = letter is not in the word\n")
    attempt = 0
    guess_list = []
    #logic loop
    while guess != wordle:
        guess = get_guess()
        while guess in guess_list:
            print("You've already guessed this! Try again.")
            guess = get_guess()
        guess_list.append(guess)
        output = evaluate_guess(guess, wordle)
        display_guess(guess, output)
        attempt = has_won(guess, wordle, attempt)
        if attempt == 6:
            print("You ran out of attempts!")
            break

    play_again = (input("Would you like to play again? Y/N: ")).upper()
    # print(wordle) for debugging

print("Thank you for playing Wordle!")




