import random

print("Welcome to the Paper, Stone, Scissor game!")

user = int(input("What do you choose? Type 0 for Paper, 1 for Stone or 2 for Scissor.\n"))

if(user >= 2):
    print("You choose Scissor.")
    print("_________________")
    print("(        ________)")
    print("(        ________)")
    print("        )")
    print("________)")
elif(user <= 0):
    print("You choose Paper.")
    print("___________")
    print("(  ________)")
    print("___)_____________")
    print("(        ________)")
    print("(        ________)")
    print("(        ________)")
    print("_________________)")
else:
    print("You choose Stone.")
    print("__________")
    print("(        _)")
    print("(        _)")
    print("(        _)")
    print("__________)")

computer = random.randint(0,2)

if(computer >= 2):
    print("Computer choose Scissor.")
    print("_________________")
    print("(        ________)")
    print("(        ________)")
    print("        )")
    print("________)")
elif(computer <= 0):
    print("Computer choose Paper.")
    print("___________")
    print("(  ________)")
    print("___)_____________")
    print("(        ________)")
    print("(        ________)")
    print("(        ________)")
    print("_________________)")
else:
    print("Computer choose Stone.")
    print("__________")
    print("(        _)")
    print("(        _)")
    print("(        _)")
    print("__________)")

if(
    (user == 0 and computer == 2) or  # Paper vs Scissor = Scissor win
    (user == 1 and computer == 0) or # Stone vs Paper = Paper win
    (user == 2 and computer == 1)   # Scissor vs Stone = Stone win
):
    print("You loose!")
elif(
    (user == 0 and computer == 1) or # Paper vs Stone = Paper win
    (user == 1 and computer == 2) or # Stone vs Scissor = Stone win
    (user == 2 and computer == 0)  # Scissor vs Paper = Scissor win
):
    print("You win!")
else:
    print("It's a draw!")