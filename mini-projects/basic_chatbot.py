bot_name: str = input("What would you like to call me?: ")
print(f'Hello! I\'m {bot_name}! How can I assist you today?')

def add(a,b):
    add = a + b
    return add

def sub(a,b):
    sub = a - b
    return sub

def mul(a,b):
    mul = a * b
    return mul

def div(a,b):
    div = a / b
    return div

def numbers():
    try:
        num1: float = float(input("Enter First number: "))
        num2: float = float(input("Enter Second number: "))
        return num1,num2
    except ValueError:
        print(f"{bot_name}: Oops! That doesm\'t seem like a valid number. Try again!")

operations = {
    "add": ("addition", add),
    "+": ("addition", add),
    "sub": ("subtraction", sub),
    "-": ("subtraction", sub),
    "mul": ("multiplication", mul),
    "*": ("multiplication", mul),
    "x": ("multiplication", mul),
    "div": ("division", div),
    "/": ("division", div),
}

while True:
    user_input: str = input('You: ').lower()

    if user_input in ["hi","hello"]:
        print(f'{bot_name}: Hi there! How can I help you?')
    elif user_input in ['bye','see you']:
        print(f'{bot_name}: Bye! Hope to see you again soon.')
        break
    elif user_input in operations:
        op_name, func = operations[user_input]
        print(f'{bot_name}: Sure, let\'s do some {op_name}! \n Please enter the two numbers below.')
        a,b=numbers()
        print(f'{bot_name}: The sum is {func(a,b)}')
        
    else:
        print(f"{bot_name}: I'm sorry, I don't understand that. Please try again.")