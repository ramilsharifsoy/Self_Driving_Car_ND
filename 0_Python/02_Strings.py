import re

R = 'RAMIL' # String created
print(len(R))
print(R[0])
print(R[3])
print(R[-1])
print(R[len(R)-1])
print(R + ' SOY')
print('SH' + R[3:])

S = 'shrubbery, ,delicious'
L = list(S) #list crated
print(L)

L[1] = 'c'
J = ''.join(L)
print(J)
print(L)
print(S.find('bb'))
print(S.replace('bb', 'cc'))
print(S)
print(S.split(','))
print(S.upper())
print(S.isalpha())

Format1 = '%s, vehicle, is %s' %('Autonomous', 'cool')
Format2 = '{0}, vehicle, is {1}'.format('Autonomous', 'cool')
Format3 = '{}, vehicle, is {}'.format('Autonomous', 'cool')
print(Format1)
print(Format2)
print(Format3)

print(dir(Format1)) # attributes of string (Format1 is a string)

help(Format1.replace) # help for explanation


print('S\nB\tC\0D') # n end, t tab, 0 binary 0 bite


match = re.match('Hello[ \t]*(.*)world', 'Hello      Python world')
final = match.group(1)
print(final)
