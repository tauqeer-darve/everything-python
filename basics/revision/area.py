import math

radius: float = float(input("Enter the radius of the circle: "))
area: float = math.pi * pow(radius,2)
print(f"Area of the circle with radius {radius}cm is {round(area,2)}cm²")