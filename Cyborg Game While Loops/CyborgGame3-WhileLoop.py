def turn_right():
    turn_left()
    turn_left()
    turn_left()

def taapo():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        taapo()
    elif front_is_clear():
        move()

#for item in range(0,6):
#    taapo()
#print(item)