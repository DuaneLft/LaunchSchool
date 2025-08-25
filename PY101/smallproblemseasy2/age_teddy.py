# Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random
#  number between 20 and 100, inclusive.


def age(name):
    from random import randint
    age = randint(20, 100)
    print(f'\n{name.capitalize()} is {age} years old!\n')

age('teddy')

