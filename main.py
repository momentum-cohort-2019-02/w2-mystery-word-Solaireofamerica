# import random
# import re
# # read words from a file
# main_text = open('words.txt', "r").read().lower()
# main_text = main_text.split()
# user_name = input("What is your name? ")

# print("Hello, " + user_name + " are you ready to play hang- Mystery Word!")


# def guess_check(word_guess):
#     while len(word_guess) > 1 or word_guess.isdigit():
#         word_guess = input("Enter a single letter please: ").lower()


# # in theory this should set the variable play_again to true or false 
# def continue_loop():
#     play = input('Would you like to play another match? \n Enter: y/n or yes/no  \n' ).lower()
#     if play == 'y' or play == 'yes':
#         return True
#     elif play != 'y' or play != 'yes':
#         return False
#     # if play == 'y' or 'yes':
#     #     return True


# def user_guess_func(letter, comp_word, mystery):
#     if_found = False
#     if letter in comp_word:
#         if_found = True
#         for i in range(0, len(comp_word)):
#             if comp_word[i] == letter:
#                 mystery = mystery[0:i] + letter + mystery[i+1:len(mystery)]
#     return (if_found, mystery)


# def make_diff_list(main_text):
#     for word in main_text:
#         if len(word) in range(4, 7):
#             easy_list.append(word)
#         if len(word) in range(6, 9):
#             medium_list.append(word)
#         if len(word) >= 8:
#             hard_list.append(word)
#     return easy_list, medium_list, hard_list


# def comp_is_diff_list(diff, computer_list):
#     while diff == 'easy' or 'medium' or 'hard':
#         if diff == 'easy':
#             computer_list = easy_list
#             print("\n \nStarting on Easy, you aren't even trying.\n \n")
#             break
#         elif diff == 'medium':
#             computer_list = medium_list
#             print("\n \nStarting on Medium, did you go to school for this?\n \n")
#             break
#         elif diff == 'hard':
#             computer_list = hard_list
#             print("\n \nStarting on Hard, get ready to get spanked, nerd.\n \n")
#             break
#         else:
#             diff = input('Please enter the correct difficulty selector: ')
#             continue
#         return computer_list


# play_again = True


# # main gameplay loop and win/lose conditions found here
# while play_again is True:
#     # takes in the difficulty, generates blank diff lists and then passes them through the function that checks the lenght of the word and appends it to each specific difficulties list
#     difficulty = input("What difficulty would you like to play on? 'Select: \n  Easy, \n  Medium, \n or Hard \n").lower()
#     easy_list = []
#     medium_list = []
#     hard_list = []
#     easy_list, medium_list, hard_list = make_diff_list(main_text)
#     # makes the blank comp_list and runs that through the function that changes the comp list based on the difficulty
#     comp_list = []
#     comp_is_diff_list(difficulty, comp_list)

#     previous_guesses_list = []

#     # filters words of a certain size into a list based on the difficulty

#     #     computer_list = []

#     computer_word = None
#     # for letter in computer_word:
#     # generate a random item from a list, detects the difficulty and then picks a word based on that difficulties word list

#     while difficulty:
#         computer_word = random.choice(comp_list)
#         print("The mystery word is " + str(len(computer_word)) + " characters long.")

#     # the old way I selected the word based off of difficulty
#     # while difficulty == 'easy' or 'medium' or 'hard':
#     #     if difficulty == 'easy':
#     #         computer_word = random.choice(easy_list)
#     #         print("The mystery word is " + str(len(computer_word)) + " characters long.")
#     #         break
#     #     elif difficulty == 'medium':
#     #         computer_word = random.choice(medium_list)
#     #         print("The mystery word is " + str(len(computer_word)) + " characters long.")
#     #         break
#     #     elif difficulty == 'hard':
#     #         computer_word = random.choice(hard_list)
#     #         print("The mystery word is " + str(len(computer_word)) + " characters long.")
#     #         break

#     # this displays the hidden version of the computer word and checks if the guessed letter is in the computers word and stores it to previous guesses
#     mystery_word = re.sub('[a-zA-Z]', '_', computer_word)

#     turns = 8
# # main gameplay loop. calls the user guess function and the continue loop function. 
#     while turns > 0:
#         user_guess = input("Enter your guess: ").lower()
#         guess_check(user_guess)
#         letter_found, mystery_word = user_guess_func(user_guess, computer_word, mystery_word)
#         if not letter_found:
#             turns -= 1
#             print("\n A swing and a miss! You have " + str(turns) + " guesses left" "\n " + mystery_word)
#         elif letter_found:
#             turns -= 1
#             print("\n You got one, it will be your last. \n You have " + str(turns) + " guesses left.")
#             print(mystery_word)
#         if "_" not in mystery_word:
#             play_again = False
#             print('\n' + computer_word + "\n Surprising. Time to up the difficulty, you won.")
#             print("You had " + str(turns) + " remaining.")
#             game_finished = True
#         if turns == 0:
#             play_again = False
#             print("\n That's the game! The word was " + computer_word + ". See ya next time. ")
#             game_finished = True
#     if game_finished:
#         play_again = continue_loop()
