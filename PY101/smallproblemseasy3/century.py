'''Write a function that takes a year as input and returns the century. The return value should be a string that begins with the 
   century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

   New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.
'''
def century_finder(year):
    century = year // 100 + 1
    if year % 100 == 0:
        century -= 1
    def suffix(number):
        last_two = str(number)[-2:]
        match last_two:
            case '11' | '12' | '13':
                return 'th'
        match str(number)[-1]:
            case '1':
                return 'st'
            case '2':
                return 'nd'
            case '3':
                return 'rd'
            case _:
                return 'th'
    return str(century) + suffix(century)

print(century_finder(2000) == "20th")           
print(century_finder(2001) == "21st")          
print(century_finder(1965) == "20th")           
print(century_finder(256) == "3rd")             
print(century_finder(5) == "1st")               
print(century_finder(10103) == "102nd")         
print(century_finder(1052) == "11th")           
print(century_finder(1127) == "12th")          
print(century_finder(11201) =="113th")        
    
    #
    
    
    

