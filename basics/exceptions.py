a, b = 10, '15'

#Exception Handling
try:
    print(a + b)
except TypeError as e: #Catching TypeError, use Exception to catch all errors(Bad Practice though!)
    print(f'Something went wrong: {e}')
    print('Please enter number as integer or float')
except Exception as e: #Allows multiple except statements for broader error handling
    print(f'Something else went wrong: {e}')

#Do not use Exception as e during development!

print('Continuing with the program...')