#Build a program that displays when the user will retire and how many years she has to work till retirement.
from datetime import date
age = int(input('What is your age? \n'))
ret = int(input('At what age would you like to retire?\n'))
print(f'''It\'s {date.today().year}. You will retire in {date.today().year + (ret - age)}.\n
You have only {ret - age} years of work to go!\n''')













                