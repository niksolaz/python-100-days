
print("Welcome to the Love Calculator!")

# Get the names
name_1 = input("Insert name 1? \n")
name_2 = input("Insert name 2? \n")
# Concatenate the names
name_concact = name_1 + name_2

# Convert the names to lowercase
names = name_concact.lower()

# Count the number of times the letters in TRUE appear
t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")

# Count the number of times the letters in LOVE appear
l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

# Concatenate the counts
trueName = str(t + r + u + e)
loveName = str(l + o + v + e)

# take the total and convert to int
total = int(trueName + loveName)

print(total)
if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")



