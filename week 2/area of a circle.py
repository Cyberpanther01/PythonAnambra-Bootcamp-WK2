# 3. A program to calculate the Area of a circle

import math

def area(radius):
    # radius = float(input("Enter the radius of the circle:" ))
    area = math.pi * radius**2
    return area

area_of_circle = area(radius= 5)
print(f'The area of the circle is {area_of_circle}')