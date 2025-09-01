# Write a function that takes a string argument and returns a new string that contains the value of the
#  original string with all consecutive duplicate characters collapsed into a single character.

def duplicate_erase(str):
    new_str = ''
    index = 0
    while index < len(str):
        if index == len(str) - 1 or str[index] != str[index + 1]:
            new_str += str[index]
        index += 1
    return new_str

# These examples should all print True
print(duplicate_erase('ddaaiillyy ddoouubbllee') == 'daily double')
print(duplicate_erase('4444abcabccba') == '4abcabcba')
print(duplicate_erase('ggggggggggggggg') == 'g')
print(duplicate_erase('abc') == 'abc')
print(duplicate_erase('a') == 'a')
print(duplicate_erase('') == '')

    