# simple f-string examples

name: str = "John"
age: int = 20

# basic
msg: str = f"My name is {name}"

# multiple values
msg2: str = f"My name is {name} and I am {age}"

# expression
msg3: str = f"Next year I will be {age + 1}"

# print
print(msg)
print(msg2)
print(msg3)