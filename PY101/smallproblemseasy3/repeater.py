#Write a function that takes two arguments, a string and a positive integer, then prints the string 
# as many times as the integer indicates.
def repeater(str, number):
  for num in range(number):
    print(str)
    
repeater('Hello', 3)