import math


def paint_cal(hieght, width, cover):
    area = hieght * width
    num_of_points = math.ceil(area / cover)
    print(f"You will need {num_of_points} cans of paint.")


test_h = int(input("Hieght of wall : "))
test_w = int(input("Width of wall : "))

coverage = 5
paint_cal(hieght=test_h, width=test_w, cover=coverage)
