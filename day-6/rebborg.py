# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Fvaria_en.json&name=Alone&url=%2Fworlds%2Ftutorial_en%2Falone.json
def move():
    pass

def turn_left():
    pass

def moved(n):
    for n in range(0,int(n)):
        move()

def turn_u(direction = 'l'):
    if direction == 'l':
        turn_left()
        turn_left()
    elif direction == 'r':
        turn_left()
        turn_left()
        turn_left()
    else:
        turn_left()
        turn_left()
        turn_left()
        turn_left()
    
moved(3)
turn_u('l')
moved(1)
turn_u('r')
moved(6)
turn_u()
moved(3)
turn_u('r')