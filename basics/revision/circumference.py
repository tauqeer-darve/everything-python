import math

radius: float = float(input("Enter the radius of the circle: "))
c: float = 2 * math.pi * radius
print(f"The Circumference of a circle with radius {radius}cm is: {round(c,2)}cm")