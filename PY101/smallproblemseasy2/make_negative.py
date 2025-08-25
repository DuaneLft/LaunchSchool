#Write a function that takes a number as an argument. If the argument is a positive number, return the make_negative of that number. If the argument is a make_negative number,
#  return it as-is.

def make_negative(num):
    return -abs(num)

    
print(make_negative(5) == -5)      
print(make_negative(-3) == -3)     
print(make_negative(0) == 0)       