import random
# Let the user choose a level of difficulty at the beginning of the program. Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters.

# At the start of the game, let the user know how many letters the computer's word contains.

# Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it should not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.

# Let the user know if their guess appears in the computer's word.

# Display the partially guessed word, as well as letters that have not been guessed. For example, if the word is BOMBARD and the letters guessed are a, b, and d, the screen should display:
# B _ _ B A _ D

# A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.

# A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's word, they do not lose a guess.

# If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.

# The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses, reveal the word to the user when the game ends.

# When a game ends, ask the user if they want to play again. The game begins again if they reply positively.

#----------------------------------------------------------------------------

# read words from a file

main_text = open('words.txt', "r").read().split()



# def difficulty_selector(biglist):
#    easy_list = if len(main_list) > 3 and < 7

# function that takes input and displays in a specific format

# generate a random item from a list

# take letter from user- normalize it- check if it's valid

user_name = input("What is your name? ")

print("Hello, " + user_name + "are you ready to play hang- Mystery Word!")

difficulty = input("What difficulty would you like to play on? 'Select:\n Easy \n Medium \n or Hard \n")
difficulty = difficulty.casefold()

easy_list = []

medium_list = []

hard_list = []
# filter a list by string size
# filters words of a certain size into a list based on the difficulty
for word in main_text:
    if len(word) in range(4, 7):
        easy_list.append(word)
    if len(word) in range(6, 9):
        medium_list.append(word)
    if word >= 8:
        hard_list.append(word)

computer_list = None

playing = input("If you would like to play again, enter 'y' ").casefold()
while difficulty is True:
    if difficulty == 'easy':
        computer_list = easy_list
        print("Starting on Easy, you aren't even trying.")
    if difficulty == 'medium':
        computer_list = medium_list
        print("Starting on Medium, did you go to school for this?")
    if difficulty == 'hard':
        computer_list = hard_list
        print("Starting on Hard, get ready to get spanked, nerd.")
    else:
        difficulty = input('Please enter the correct difficulty selector: ').casefold()
# --------------------------------------------------------------------------
computer_word = None

user_guess = None

turns = 8

while turns > 0:
    falied = 0
    for char in computer_word:
        if char in user_guess:
            print(char)
        else:
            print('_'),
            falied += 1
    