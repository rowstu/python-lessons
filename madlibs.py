
# Teaching the kids Python print with madlibs

adjective = input('Please enter a descriptive word: ')
adjective2 = input('Please enter an emotional feeling: ')
verb1 = input('Please enter a doing word: ')
verb2 = input('Please enter another doing word unrealted to the first: ')
name = input("Please enter a person's name:")

madlib = f'''

Python programming is so {adjective}!
It makes me feel so {adjective2}.
I also love to spend my time {verb1}. 
So it's best to stay hydrated.
When I'm not programming, I like to spend my time
{verb2} with {name}

'''

print(madlib)
