import math as m

a: float = float(input("Enter side A: "))
b: float = float(input("Enter side B: "))

c: float = m.sqrt(pow(a,2) + pow(b,2))

print(f"Hypotenuse(side C) of Triangle with sides {a} and {b} is {round(c,2)}")