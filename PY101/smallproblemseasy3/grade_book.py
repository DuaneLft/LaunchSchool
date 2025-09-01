'''Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.

Numerical score letter grade list:

90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'
0 <= score < 60: 'F'
Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.
'''
def get_grade(one, two, three):
    average = (one + two + three)/3
    match average:
        case _ if 90 <= average <= 100:
            return 'A'
        case _ if 80 <= average < 90:
            return 'B'
        case _ if 70 <= average < 80:
            return 'C'
        case _ if 60 <= average < 70:
            return 'D'
        case _ if 0 <= average < 60:
            return 'F'
        case _:
            print('You entered incorrect data!')

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
        
