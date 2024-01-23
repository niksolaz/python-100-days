# prime checker

def prime_checker(number):
    is_prime = True
    divisible = []
    if type(number) != int:
        print(f"{number} is not a number")
        return False, []
    if number < 2:
        is_prime = False
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            divisible.append(i)

    if is_prime:
        print(f"{number} is a prime number")
        return True, []
    else:
        print(f"{number} is not a prime number: {divisible}")
        return False, divisible

# n = int(input("Check this number: "))
# prime_checker(number=n)