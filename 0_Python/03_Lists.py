
L = [123, "spam", 1.23]
print(len(L))
print(L[0])
print(L[:-1])
NewL = L + [4, 5, 6]
print(NewL)
print(L*3)
print(L) #original didnot change
L.append('NI')
L.pop(2)
print(L)


M = ['bb', 'cc', 'aa']
M.sort()
print(M)

M.reverse()
print(M)


N = [[1, 2, 3],
     [4 ,5 ,6],
     [7 ,8 ,9]]

print(N)

row2 = N[1]
print(row2)

row2_3rd = N[1][2]
print(row2_3rd)

col2 = [row[1] for row in N]
print(col2)

col2add1 = [row[1] + 1 for row in N]
print(col2add1)

diag = [N[i][i] for i in [0, 1, 2]]
print(diag)

doubles = [2*c for c in 'spam']
print(doubles)

rnge = list(range(4))
print(rnge)

increm = list(range(-6, 7, 2))
print(increm)

multivalue = [[x**2, x**3, x**4] for x in range(4)]
print(multivalue)

multicrem = [[x, x/2, x*2] for x in range(-6, 7, 2) if x > 0]
print(multicrem)

G = (sum(row) for row in N) #Gnerator
print(next(G))
print(next(G))
print(next(G))

mapsums = list(map(sum, N)) # == G
print(mapsums)

ordinances_list = [ord(x) for x in 'spaam']
ordinances_sets = {ord(x) for x in 'spaam'} #dublicates removed
ordinance_dictionary = {x: ord(x) for x in 'spaam'}

print(ordinances_list)
print(ordinances_sets)
print(ordinance_dictionary)
