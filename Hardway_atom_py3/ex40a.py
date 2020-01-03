'''
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# this goes in mystuff.py
def apple():
    print("I AM APPLES!")

import mystuff
mystuff.apple()

def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of a dream"

import mystuff

mystuff.apple()
print(mystuff.tangerine)

mystuff['apple'] # get apple from dict  #呢個係變量
mystuff.apple() # get apple from the module #呢個係(mystuff檔名).py
mystuff.tangerine # same thing, it's just a variable  #呢個係(mystuff檔名).py

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
'''
