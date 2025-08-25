"""
Create a function that takes 2 arguments, a list and a dictionary. The list will contain 2 or more elements
 that, when joined with spaces, will produce a person's name. The dictionary will contain two keys,
 "title" and "occupation", and the appropriate values. Your function should return a greeting that uses
 the person's full name, and mentions the person's title.

 Hello, John Q Doe! Nice to have a Master Plumber around.

"""
occupation = {'title': 'Junior Level', 'occupation': 'Software Developer'}
person = ['Raleigh', 'D', 'Leftwich']

def greetings(name, job):
    return f'Hello, {' '.join(name)}! Nice to have a {job['title']} {job['occupation']} around.'


print(greetings(person, occupation))
    