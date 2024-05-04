def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
        
# for race in range(1, 7):
#     each_hurdle()

# no_of_hurdles = 0
# while no_of_hurdles < 6:
#     each_hurdle()
#     no_of_hurdles += 1

# Hurdle 2
# while at_goal() == False:
#     each_hurdle()

# OR
# while not at_goal():
#     each_hurdle()
    
# OR
while at_goal() != True:
    jump()
    
# Hurdle 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def front_is_clear():
    move()
    
def wall_in_front():
    jump()
    
while at_goal() != True:
    if front_is_clear() == True:
        front_is_clear()
    else:
        wall_in_front()

# Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right == True:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear == True:
        move()
    turn_left()
    
while at_goal() != True:
    if front_is_clear() == True:
        move()
    else: # wall_in_front
        jump()
        
# Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()

""" def jump():
    turn_left()
    while wall_on_right == True:
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear == True:
        move()
    turn_left() """
    
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
    elif right_is_clear():
        turn_right()
    else:  # wall_on_right()
        move()
        
# OR
""" while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left() """

    
