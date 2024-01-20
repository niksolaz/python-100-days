# adding even numbers exercise

def add_even_numbers():  
    choose_number = int(input("Choose number between 1 and 100: "))

    if choose_number > 100:
        print("Number is greater than 100")
        add_even_numbers()
    elif choose_number < 1:
        print("Number is less than 1")
        add_even_numbers()
    else :
        sum = 0
        for number in range(1, choose_number + 1):
            if number % 2 == 0:
                sum += number
        print(f"Sum of even numbers between 1 and {choose_number} is {sum}")

add_even_numbers()