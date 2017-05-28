


# Object Types         Example Litterals/Creation

#           Immutable
# Numbers                1234, 3.1415, ...
# Strings                'spam', "Bob's", ...  
# Tuples                 (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
#        Not Immutable
# Dictionaries           {'food': 'spam', 'taste' : 'yum'}, dict(hours=10)
# Lists                  [1,[2, 'three'], 4.5], list(range(10))
# Sets                   set('abc'), {'a', 'b', 'c'}

# Files                  open('eggs.txt'), open(r'C:\ham.bin', 'wb')
# Other core types       Booleans, types, none
# Programs < Modules < Statements < Expressions (create and process) < Objects


import math
import sys
import random

print('Hello World')
print('Spam! ' * 8)
print(2 ** 100) #to the power of
print(math.pi) # pi im module math
print(math.sqrt(math.pi))
print(random.random())
print(random.choice([1, 2, 3, 4]))