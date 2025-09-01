'''A double number is an even-length number whose left-side digits are exactly the same as its right-side
 digits. For example, 44, 3333, 103103, and 7676 are all double numbers, whereas 444, 334433, and 107 are not.

Write a function that returns the number provided as an argument multiplied by two, unless the argument is a
 double number. If the argument is a double number, return the double number as-is.'''

def twice(number):
    num = str(number)
    if num[0:len(num)//2] == num[len(num)//2:len(num)]:
        return number
    else:
        return number * 2

print(twice(37) == 74)                  
print(twice(44) == 44)                  
print(twice(334433) == 668866)          
print(twice(444) == 888)                
print(twice(107) == 214)                
print(twice(103103) == 103103)          
print(twice(3333) == 3333)              
print(twice(7676) == 7676)              