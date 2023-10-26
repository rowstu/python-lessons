
# more advanced madlibs
# text borrowed and modified from here:
# https://pythonscholar.com/python-projects/mad-libs-game-in-python/

verb_1 = input('Enter a verb of choice, and press enter: ')
adj_1 = input('Enter a adjective of choice, and press enter: ')
verb_2 = input('Enter second verb of choice, and press enter: ')
body_part = input('Enter a body part name of choice, and press enter: ')
adverb = input('Enter an adverb of choice, and press enter: ')
body_part_2 = input('Enter any body name of your choice,and press enter: ')
noun = input('Enter an animal of choice, and press enter: ')
verb_3 = input('Enter the third verb of choice, and press enter: ')
animal = input('Enter name of any animal of choice, and press enter: ')
noun_2 = input('Enter an noun of choice , and press enter: ')
verb_4 = input('Enter the fourth verb of choice, and press enter: ')
adj_2 = input('Enter an adjective of chioce, and press enter :')
colour = input('Enter any color name, and press enter: ')


madlib = f'''

Most doctors agree that {verb_1}ing is a/an {adj_1} form of exercise. 
{verb_2} on a bicycle enables you to develop your {body_part} muscles 
as well as {adverb} increase the rate of a {body_part_2} beat. 
More {noun} around the world {verb_3} bicycles than drive {animal}. 
No matter what kind of {noun_2} you {verb_4}, always be sure to wear a/an {adj_2} helmet. 
Make sure to have  {colour}  reflectors too!


'''

print(madlib)
