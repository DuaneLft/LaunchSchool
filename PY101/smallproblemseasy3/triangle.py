#Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides
#  each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have
#  one end at the lower-left of the triangle, and the other end at the upper-right.

def triangle(size):
    character_count = 1
    shape = '*'
    space = ' '
    white_space = size - 1
    for num in range(1,size + 1):
        print(space * white_space + shape * character_count)
        character_count += 1
        white_space -= 1
    

triangle(5)
triangle(9)