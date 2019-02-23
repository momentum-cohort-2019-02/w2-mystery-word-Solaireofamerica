main_text = open('words.txt', "r").read().lower()
main_text = main_text.split()
user_name = input("What is your name? ")

comp_word = 'maximize'
user_guess = ''
prev_guess = []
your_guess = input("Enter one letter for a guess: ")


def checks_word(user_guess, comp_word, prev_guesses):
    for letter in comp_word:
        if user_guess in comp_word:
            prev_guess.append(user_guess)
        


checks_word(your_guess, comp_word, prev_guess)
