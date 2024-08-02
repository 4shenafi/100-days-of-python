import math 
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = int(input("Coverage: "))

def paint_clac(test_h, test_w, coverage):
    paint_needed = test_h * test_w / coverage
    return math.ceil(paint_needed)

print(f'You\'ll need {paint_clac(test_h, test_w, coverage)} cans of paint.')