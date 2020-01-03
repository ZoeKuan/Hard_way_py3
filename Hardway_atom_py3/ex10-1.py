# ex10-1.py

#2. change ''' to """

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass.
'''

print (fat_cat)

#3. escape sequences > format string

formatter = "{} {} {}"
a = "\a1, \b2, \ff3"
b = "\N{name}1, \r2, \v333"

#print(formatter.format(a))
print(formatter.format(b))
