print("The paint calulator\n".upper())

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    from math import ceil       # OR import math
    number_of_cans = ceil(number_of_cans)       # nummber_of_cans = math.ceil(number_of_cans) 
    if number_of_cans == 1:
        print("A can of paint is needed.")
    elif number_of_cans >= 2:
        print(f"{number_of_cans} cans are needed for the wall.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)