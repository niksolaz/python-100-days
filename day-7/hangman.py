# hangman
import random # import random module

word_list = ["topolino", "paperino", "batman", "superman"] # list of words
choose_word = random.choice(word_list) # choose random word from list
display = [] # empty list
letters_wrong = [] # empty list

def start(): # function
    print("Welcome to Hangman") # print welcome message
    print("  _______")
    print("  |     |")
    print("  |      ")
    print("  |      ")
    print("  |      ")
    print("__|__")
    print("your possibility are 6")

def stage(): # function
    index = len(letters_wrong) # increment the index variable
    if index == 1:
        print("  _______")
        print("  |     |")
        print("  |     O")
        print("  |      ")
        print("  |      ")
        print("__|__")
    elif index == 2:
        print("  _______")
        print("  |     |")
        print("  |     O")
        print("  |     |")
        print("  |      ")
        print("__|__")
    elif index == 3:
        print("  _______")
        print("  |     |")
        print("  |     O")
        print("  |     |\\")
        print("  |      ")
        print("__|__")
    elif index == 4:
        print("  _______")
        print("  |     |")
        print("  |     O")
        print("  |    /|\\")
        print("  |      ")
        print("__|__")
    elif index == 5:
        print("  _______")
        print("  |     |")
        print("  |     O")
        print("  |    /|\\")
        print("  |      \\")
        print("__|__")
    elif index == 6:
        print("  _______")
        print("  |     |")
        print("  |     O")
        print("  |    /|\\")
        print("  |    / \\")
        print("__|__")
    print(f"You have ", {6 - index}, " possibility")
    if index == 6:
        print("GAME OVER")
        exit()
    else:
        hangman()

for letter in choose_word: # loop through the word
    display.append("_") # add _ to the list

start()
print(display) # print the list

def hangman(): # function
    guess = input("Guess a letter: ").lower() # ask user to guess a letter
    exist_letter = False # boolean variable
    for position in range(len(choose_word)): # loop through the word
        letter = choose_word[position] # get the letter at the position
        if letter == guess: # if the letter is the same as the guess
            display[position] = letter.upper() # replace the _ with the letter
            print("Good guess: \n", "".join(display)) # print the list again
            print(display)
            exist_letter = True # change the boolean variable to True

    if not exist_letter:
        print("Wrong guess: \n", "".join(display))
        print(display)
        letters_wrong.append(guess)
        stage()

    if "_" in display:
        hangman()
    else:
        print("You win")
        exit()


hangman() # call the function