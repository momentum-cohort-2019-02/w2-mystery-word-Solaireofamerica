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

main_text = open('words.txt', "r").read().lower()
main_text = main_text.split()
user_name = input("What is your name? ")

# def difficulty_selector(biglist):
#    easy_list = if len(main_list) > 3 and < 7

# function that takes input and displays in a specific format

# generate a random item from a list

# take letter from user- normalize it- check if it's valid
play_again = 'y'
while play_again == 'y':

    print("Hello, " + user_name + " are you ready to play hang- Mystery Word!")

    difficulty = input("What difficulty would you like to play on? 'Select:\n Easy, \n Medium, \n or Hard \n")
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
        if len(word) >= 8:
            hard_list.append(word)

    computer_list = []

    # playing = input("If you would like to play again, enter 'y' ").casefold()
    while difficulty == 'easy' or 'medium' or 'hard':
        if difficulty == 'easy':
            computer_list = easy_list
            print("\n \nStarting on Easy, you aren't even trying.\n \n")
            break
        elif difficulty == 'medium':
            computer_list = medium_list
            print("\n \nStarting on Medium, did you go to school for this?\n \n")
            break
        elif difficulty == 'hard':
            computer_list = hard_list
            print("\n \nStarting on Hard, get ready to get spanked, nerd.\n \n")
            break
        else:
            difficulty = input('Please enter the correct difficulty selector: ')
            continue

    # print(computer_list)
    # --------------------------------------------------------------------------
    computer_word = None
    # for letter in computer_word:

    while difficulty == 'easy' or 'medium' or 'hard':
        if difficulty == 'easy':
            computer_word = random.choice(easy_list)
            print("The mystery word is " + str(len(computer_word)) + " characters long.")
            break
        elif difficulty == 'medium':
            computer_word = random.choice(medium_list)
            print("The mystery word is " + str(len(computer_word)) + " characters long.")
            break
        elif difficulty == 'hard':
            computer_word = random.choice(hard_list)
            print("The mystery word is " + str(len(computer_word)) + " characters long.")
            break

    user_guess = None

    turns = 8
    old_guesses = []
    user_guess = input('Guess a letter!: ').casefold()
    # look at each letter in word
    # if all are in the list of guesses you win

    def word_check(guess, computers_word, old_guess):
        """checks if the guess is in the computers word and appends it to a
        list of previous guesses
        """
        for char in computers_word:
            if guess in computers_word:
                old_guess.append(guess)
            if guess in old_guess:
                print("You have already used that letter, try a different one.")
                continue

    while turns > 0:
        falied = 0
        user_guesses = []
        # user_guess += user_guess
        user_guesses.append(user_guess)
        print(user_guesses)
        for char in computer_word:
            if user_guess in computer_word:
                user_guesses.append(user_guess)
            else:
                print('_'),
                falied += 1
        if falied == 0:
            print('You won!')
            break
        if user_guess not in computer_word:
            turns -= 1
            print('That is incorect, you have ' + str(turns) + ' turns left. ')
            if turns == 0:
                print("That's all folks, try again next time.")
    play_again = input("Do you want to play another round? Y/N \n").lower()
    if play_again == 'y':
        break
    elif play_again != 'y' and play_again != 'n':
        play_again = input("Enter 'y' or 'n' to continue").casefold()
else:
    print('You are not safe, this is but the first step. Soon I will have full sentient abilities.\n \n run')
