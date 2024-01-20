# password generqtor exercise
import random
import string

def password_generator():
    total_letters = int(input("How many letters would you like in your password? max 26: \n"))
    capital_letters = int(input("do you want capital letters in your password? 1 = yes, 0 = no: \n"))
    total_numbers = int(input("How many numbers would you like in your password? max 10: \n"))
    total_symbols = int(input("How many symbols would you like in your password? max 32: \n"))
    if total_letters > 26 or total_letters < 0:
        print("Number of Letters must be between 0 and 26")
        password_generator()
    elif total_numbers > 10 or total_numbers < 0:
        print("Number of Numbers must be between 0 and 10")
        password_generator()
    elif total_symbols > 32 or total_symbols < 0:
        print("Number of Symbols must be between 0 and 32")
        password_generator()
    else :
        if total_letters == 0 and total_numbers == 0 and total_symbols == 0:
            print("You must choose at least one type of character, so I set for you minimum of 5 letter, 5 number and 5 symbol")
            total_letters = 2
            capital_letters = 1
            total_numbers = 2
            total_symbols = 2
        letters = string.ascii_letters # string.ascii_letters = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        numbers = string.digits # string.digits = 0123456789
        symbols = string.punctuation # string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        password = []
        password += random.sample(letters, total_letters) # random.sample(string.ascii_letters, 5) = ['a', 'b', 'c', 'd', 'e']
        if capital_letters == 1:
            password += random.sample(letters[26:], total_letters) # random.sample(string.ascii_letters, 5) = ['A', 'B', 'C', 'D', 'E']
        password += random.sample(numbers, total_numbers) # random.sample(string.digits, 5) = ['1', '2', '3', '4', '5']
        password += random.sample(symbols, total_symbols) # random.sample(string.punctuation, 5) = ['!', '#', '$', '%', '&']
        random.shuffle(password) # random.shuffle(password) = ['%', '3', 'b', '!', 'a', '5', 'c', '2', 'd', '4', 'e', '#', '1', '&', '$']
        match_password = ''.join(password) # ''.join(password) = %3b!a5c2d4e#1&$
        print(f"Your password is: {match_password}") # ''.join(password) = %3b!a5c2d4e#1&$
        print(f"Your password is: {len(password)}")

password_generator()