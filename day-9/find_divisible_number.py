"""
Find divisible number
"""

def find_divisible_number(number):
    list_divisible = []
    if type(number) != int:
        print(f"{number} is not a number")
        return False, []
    if number < 2:
        return False, []
    for i in range(2, (number + 1)):
        if number % i == 0:
            list_divisible.append(i)
    print(list_divisible)
    return True, list_divisible

