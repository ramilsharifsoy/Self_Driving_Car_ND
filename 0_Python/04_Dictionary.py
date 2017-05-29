#Mapping

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D)
print(D['food']) # value of key 'food'

addone = D['quantity'] + 1
print(addone)

E = {}
E['name'] = 'Ramil'
E['job'] = 'MLE'
E['age'] = 25
print(E)
print(E['name'])

ram1 = dict( name='Ramil', job='MLE', age=25)
print(ram1)

ram2 = dict(zip(['name', 'job', 'age'],['Ramil', 'MLE', 25]))
print(ram2)

#Nesting

rec = 0 # cleaned object space
print(rec)

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'jobs': ['dev', 'mgr'],
       'age': 40.5}
print(rec)
print(rec['name']) # nested dictionary
print(rec['name']['last'])

addjob = rec['jobs'].append('coach')
print(rec)

# Missing Keys: if tests
F = {'a': 1, 'b': 2, 'c': 3}
print(F)

F['e'] = 99
print(F)

if not 'f' in F:
   print('missing')

value = F.get('x', 0) # index with default
print(value)

value = F['x'] if 'x' in F else 5
print(value)

# Sorting Keys: for Loops
L = {'a': 1, 'c': 3, 'b': 2}
print(L)

for key in sorted(L):
	print(key, "=>", L[key])

for c in 'Ramil':
	print(c.upper() * 2)

i = 4
while i > 0:
	print('Python ' * i)
	i -= 1

# equivalet operations
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)

squares = []
for x in [1, 2, 3, 4, 5]:
	squares.append(x ** 2)

print(squares)