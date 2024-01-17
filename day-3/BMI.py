# calculator BMI: weight / height ** 2

# set the weight and height
weight = input("Enter your weight in kg: ")
height = input("Enter your height in m: ")

# calculate the BMI, but first convert the weight and height to float because input function returns string
bmi = float(weight) / (float(height) ** 2)

# print the BMI
print(f"Your BMI is: {bmi}")

"""
value of BMI:
Under 16 : Severely Underweight
Under 18.5: Underweight
Between 18.5 and 25: Normal
Between 25 and 29.9: Overweight
Between 30 and 34.9: Obese
Over 35: Clinically Obese
""" 

if bmi < 16:
    print("Severely Underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30 and bmi < 35:
    print("Obese")
else:
    print("Clinically Obese")
