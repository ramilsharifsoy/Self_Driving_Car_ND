
S = "Amazon Exam Question Which I Passed" #a string
no_wspace = S.rstrip()  #remove white spaces 
print (no_wspace)

no_wspace2 = S.replace(' ', '_') # replace content
print (no_wspace2)

splitted = S.split(' ') # split and turn into list
print(splitted)

findAma = S.find('Passed') # match and find and report starting location
print (findAma)

print ("Ramil says: %s" %S) # formatting 1
print ("Ramil says: {}".format(S)) # formatting 2

print (S[3]) # index 3rd

print(S[3:10]) # slice piece from 3 to 9 inclusive, 10 not
print(S[3:]) # slice piece from 3 and on
print(S[:6]) # slice piece upto 6

print(len(S)) # legth of a string

