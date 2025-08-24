# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

def odd_printer(number):
    odds = list(range(1, number + 1, 2))
    for odd in odds:
        print(odd)
    return odds

odd_printer(99)
"""
launch school answer

for number in range(1, 100):
    if number % 2 == 1:
        print(number)

for number in range(1, 100, 2):
    print(number)        
"""
              
                          
