"""
create a function that takes value from dictionary
"""

# create a dictionary of fruits with their prices
fruits = {
    "apple": 1.99,
    "banana": 0.99,
    "orange": 1.49,
    "grapes": 2.99
}

# f(x) = 1 restituisce 1 per tutti gli input
# f(x) = rand() restituisce un valore casuale
# f(x) = next_empty_slot() restituisce il prossimo slot vuoto
# f(x) = len(x) restituisce la lunghezza di x

# create a function that takes a dictionary and a key as arguments
def f(dict, key):
    return dict[key]

res = f(fruits, "orange") # 1.49

print(res) # 1.49