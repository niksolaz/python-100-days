# Description: Tip Calculator

# Instructions
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6 
# Format the result to 2 decimal places = 33.60

# floatFormat function rounds the number to 2 decimal places
def floatFormat(number):
  return round(number, 2)

# calculateTip function calculates the tip based on the bill and tip percentage
def calculateTip(bill, tipPercentage):
    return (bill * tipPercentage) / 100

# calculateTotal function calculates the total bill including the tip
def calculateTotal(bill, tip):
    return bill + tip

# calculateSplit function calculates the split amount based on the total bill and number of people
def calculateSplit(bill, people):
    return floatFormat(bill / people)

print("Welcome to the tip calculator.")
# input the bill amount, tip percentage and number of people
bill = float(input("What was the total bill? "))
# input the tip percentage
tipPercentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
tip = calculateTip(bill, tipPercentage)
total = calculateTotal(bill, tip)
# input the number of people
people = int(input("How many people to split the bill? "))
split = calculateSplit(total, people)

# print the split amount for each person
print(f"Each person should pay:: ${split}")





