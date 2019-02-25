import random
import re
# read words from a file
main_text = open('words.txt', "r").read().lower()
main_text = main_text.split()
user_name = input("What is your name? ")

print("Hello, " + user_name + " are you ready to play hang- Mystery Word!")

difficulty = input("What difficulty would you like to play on? 'Select:\n Easy, \n Medium, \n or Hard \n")
difficulty = difficulty.casefold()
easy_list = []

medium_list = []

hard_list = []

# filters words of a certain size into a list based on the difficulty
def make_diff_list(main_text):
    for word in main_text:
        if len(word) in range(4, 7):
            easy_list.append(word)
        if len(word) in range(6, 9):
            medium_list.append(word)
        if len(word) >= 8:
            hard_list.append(word)
    return easy_list, medium_list, hard_list
easy_list, medium_list, hard_list = make_diff_list(main_text)
#     computer_list = []

# playing = input("If you would like to play again, enter 'y' ").casefold()d
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

computer_word = None
# for letter in computer_word:
# generate a random item from a list, detects the difficulty and then picks a word based on that difficulties word list
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

# this displays the hidden version of the computer word and checks if the guessed letter is in the computers word and stores it to previous guesses
mystery_word = re.sub('[a-zA-Z]', '_', computer_word)

def user_guess_func(letter, comp_word, mystery):
    if_found = False
    if letter in comp_word:
        if_found = True
        for i in range(0, len(comp_word)):
            if comp_word[i] == letter:
                mystery = mystery[0:i] + letter + mystery[i+1:len(mystery)]
    return (if_found, mystery)

print(mystery_word)


def continue_loop():
    play_again = input('Would you like to play another match? \n Enter: y/n or yes/no  \n' ).lower()
    if play_again.isalpha() and len(play_again) >= 3 and play_again ==  'y' or 'yes':
        print("CAN YOU SMELL WHAT THE ROCK, IS, COOKINGGGG????")
        return True
    elif play_again.isalpha() and len(play_again) >= 2 and play_again !=  'n' or 'no':
        print("Come again, scrub.")
        return False

play_again = True
# main gameplay loop and win/lose conditions found here
turns = 8
while play_again == True:
    playing = True
    while playing == True:
        while turns > 0:
            user_guess = input("Enter your guess: ")[:1].lower()
            if len(user_guess) > 1 or user_guess.isdigit():
                user_guess = input("Enter a single letter please: ")[:1].lower()
            letter_found, mystery_word = user_guess_func(user_guess, computer_word, mystery_word)
            if not letter_found:
                turns -= 1
                print("\n A swing and a miss! You have " + str(turns) +" guesses left" "\n " + mystery_word)
            elif letter_found:
                print("\n You got one, it will be your last. \n You have " + str(turns) + " guesses left.")
                print(mystery_word)
            if "_" not in mystery_word:
                print('\n' + computer_word + "\n Surprising. Time to up the difficulty, you won. \n You had " + str(turns) + " remaining.")
                play_again = continue_loop()
                playing = False
            if turns == 0:
                print("\n That's the game! The word was " + computer_word + ". See ya next time. ")
                play_again = continue_loop()
                playing = False
        if 
    if play_again == True:
        continue
    else:
        print("Later nerd!")
        break
    