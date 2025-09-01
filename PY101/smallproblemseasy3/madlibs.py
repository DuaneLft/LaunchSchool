#Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and injects 
# them into a story that you create.
'''Enter a noun: dog
   Enter a verb: walk
   Enter an adjective: blue
   Enter an adverb: quickly


Do you verb your adjective noun adverb? That's hilarious!
The adj n v adv over the lazy n.
The n adv v up to Joe's adj turtle.
'''

noun = input('Enter a noun: \n')
verb = input('Enter a verb: \n')
adjective = input('Enter an adjective: \n')
adverb = input('Enter an adverb: \n')
print(f'\nDo you {verb} your {adjective} {noun} {adverb}? That\'s hilarious!\nThe {adjective} {noun} {verb}s '
      f'{adverb} over the lazy {noun}. The {noun} {adverb} {verb}s up to Joe\'s {adjective} turtle.\n')
