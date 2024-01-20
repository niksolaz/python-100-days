# fizzbuzz interview exercise

def fizzbuzz():
    numbers = int(input("Choose number between 2 and 100: "))
    if numbers > 100:
        print("Number is greater than 100")
        fizzbuzz()
    elif numbers < 2:
        print("Number is less than 2")
        fizzbuzz()
    else :
        fizzbuzz = []
        for number in range(1, numbers + 1):
            if number % 3 == 0 and number % 5 == 0:
                print("fizzbuzz")
                fizzbuzz.append(number)
            elif number % 3 == 0:
                print("fizz")
            elif number % 5 == 0:
                print("buzz")
            else :
                print(number)
        print(f"Number of fizzbuzz is {fizzbuzz}")

fizzbuzz()