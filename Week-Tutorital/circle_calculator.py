import math
radius = int(input("Enter the radius of the circle: "))
area = 3.14 * radius ** 2
print("The area of the circle is:", area)
circumference = 2 * 3.14 * radius
print("The circumference of the circle is:", circumference)
diameter = 2 * radius
print("The diameter of the circle is:", diameter)
area_round = round(area, 2)
print("The area of the circle is:", area_round)
circumference_round = round(circumference, 2)
print("The circumference of the circle is:", circumference_round)
area_math_pi = math.pi * radius ** 2
print("The area of the circle is:", area_math_pi)

