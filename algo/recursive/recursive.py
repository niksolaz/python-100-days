
def recursive(i):
    if i == 0:
        return 0  # caso base
    else:
        return i + recursive(i-1) # caso recursivo
    
print(recursive(5))  # 15
    