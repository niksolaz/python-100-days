# prime checker

def prime_checker(number):
    is_prime = True
    divisible = []
    if number < 2:
        is_prime = False
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            divisible.append(i)

    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number: {divisible}")

n = int(input("Check this number: "))
prime_checker(number=n)