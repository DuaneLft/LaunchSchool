# Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product of all numbers between 1 and the
# entered integer, inclusive.

print('This program will give the sumation or factorial of the integer entered. \n')
number = int(input('Please enter a whole number greater than 0.\n'))
prompt = input('Please enter s for sumation or p for factorial\n')
sum_total = 0
factorial = 1

if prompt == 's':
    for num in range(1, number + 1):
        sum_total += num
    print(f'The sum of all numbers up to {number} is: {sum_total}\n')
elif prompt == 'p':
    for num in range(1, number + 1):
        factorial *= num
    print(f'The factorial of {number} is: {factorial}\n')
else:
    print('Please start over and check your input')
    32
    


