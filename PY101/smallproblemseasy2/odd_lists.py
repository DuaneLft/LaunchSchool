# Write a function that returns a list that contains every other element of a list that is passed in as
#  an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th, and 
# so on elements of the argument list.

def odd_list(elements):
    new_list = []
    count = 0
    while count < len(elements):  
        
        value = elements[count]
        new_list.append(value)
        count += 2
        
    return new_list


print(odd_list([2, 3, 4, 5, 6]) == [2, 4, 6])  
print(odd_list([1, 2, 3, 4]) == [1, 3])        
print(odd_list(["abc", "def"]) == ['abc'])     
print(odd_list([123]) == [123])                
print(odd_list([]) == [])                      
