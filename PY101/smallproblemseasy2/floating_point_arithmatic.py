"""
Write a program that prompts the user for two positive numbers (floating-point), then prints the results of
 the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient,
   remainder, and power. Do not worry about validating the input.
"""
print('Hello user this is a program that will ask you for two positive numbers and will compute for you the following' \
'operations on the two numbers. Addition, subtraction, product, quotient, floor quotient, remainder, and power.\n')
num1 = float(input('Please enter your first number \n'))
num2 = float(input('Please enter your second number \n'))

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')
