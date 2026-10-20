from random import randint

#Selects a random word from list
def choose_word():
    word_list = ["CRANE", "SLATE", "AUDIO", "STARE", "RAISE", "PLANT", "GHOST", "SHINE", "FLAME", "BRICK"]
    num = randint(0,9)
    wordle = word_list[num]
    return wordle

#Gets and validates the input of a guess
def get_guess():
    word = (input("Please enter a 5 letter word: ")).upper()
    word_length = len(word)
    while word_length != 5:
        print("Your guess must be exactly 5 letters.")
        word = (input("Please enter a 5 letter word: ")).upper() 
        word_length = len(word) 
    guess = word.upper()
    return guess

#Logic of the wordle game to see how close the word was and outputs a string
def evaluate_guess(guess, wordle):
    output = ""    
    for letter in range(5):
        if guess[letter] == wordle[letter]:
            output = output + " G"
        elif guess[letter] in wordle:
            output = output + " Y"
        else:
            output = output + " -"
    return output

#Displays the users guess feedback
def display_guess(guess, output):
    spaced_guess = ""
    for letter in range(5):
        spaced_guess = spaced_guess + " " + guess[letter]
    print(f"Guess:    {spaced_guess}")
    print(f"Feedback: {output}")

#Keeps track of the user's tries and gives final feedback when the game is complete
def has_won(guess, wordle, attempt):
    if guess != wordle:
        attempt += 1
        print(f"Attempt {attempt} of 6")
    else:
        attempt += 1
        print(f"Congratulations! You solved the puzzle in {attempt} attempt(s)!")
    return attempt
    





