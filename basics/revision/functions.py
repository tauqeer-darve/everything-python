def func() -> None:
    print('Hello')

func()
func()


def add(a: float, b: float) -> float:   # function takes 2 floats, returns float
    print(f'Adding: {a} + {b}')         # f-string to show operation
    return a + b                        # return sum

print(add(a=10, b=15))                  # call with named args → 25
print(add(a=15, b=30))                  # call with named args → 45


def greet(name: str, greeting: str = 'Hi') -> None:  # name required, greeting default
    print(f'{greeting}, {name}!')      # print greeting message

greet('Bob', 'Ciao')                   # override default greeting
greet('James')                         # uses default 'Hi'