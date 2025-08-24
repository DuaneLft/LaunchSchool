# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.
# Note: 1 square meter == 10.7639 square feet

length = float(input('Please enter the length of your room in meters. \n'))
width = float(input('Now enter the width of your room in meters. \n'))
print(f'The area of your room is {length * width} square meters or {(length * width) * 10.7639} square feet')

