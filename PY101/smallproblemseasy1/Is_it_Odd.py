# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise

def is_odd(number):
    if type(number) != int:
        print('Please enter an integer value')
        return TypeError
    if abs(number) % 2 == 0:
        return False
    else:
        return True
    


# This is lauch schools answer
"""
def is_odd(number):
    return abs(number) % 2 == 1
    """