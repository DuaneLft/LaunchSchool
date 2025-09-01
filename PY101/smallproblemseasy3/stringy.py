#Write a function that takes one argument, a positive integer, and returns a string of alternating 
# '1's and '0's, always starting with a '1'. The length of the string should match the given integer.

def stringy(number):
    bits = ''
    for num in range(1, number + 1):
        if num % 2 == 0:
            bits += '0'
        else:
            bits += '1'
    return bits


print(stringy(6) == "101010")           
print(stringy(9) == "101010101")        
print(stringy(4) == "1010")             
print(stringy(7) == "1010101")          