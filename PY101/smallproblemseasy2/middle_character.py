#Write a function that takes a non-empty string argument and returns the middle character(s) of the string.
#  If the string has an odd length, you should return exactly one character. If the string has an even length,
#  you should return exactly two characters.

def str_middle(char):
    length = len(char)
    if length % 2 == 0:
        return char[int(length/2 -1):int(length/2 +1)]
    elif length == 1:
        return char
    else:
        return char[int(length//2)]
    
print(str_middle('I Love Python!!!') == "Py")    # True
print(str_middle('Launch School') == " ")        # True
print(str_middle('Launchschool') == "hs")        # True
print(str_middle('Launch') == "un")              # True
print(str_middle('Launch School is #1') == "h")  # True
print(str_middle('x') == "x")                    # True