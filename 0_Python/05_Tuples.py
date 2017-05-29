# immutable list
T = (1 ,2 ,3 , 4)
length = len(T)
print(T)
print(length)

Concatination = T + (5, 6)
print(Concatination)

index0 = T[0]
print(index0)

at4 = T.index(4)
print(at4)

howmany4 = T.count(4)
print(howmany4)

Tnew = (2,3,) + T[1:]
print(Tnew)
print(T)

T_mixed_nesting = 'spam', 3.0, [11, 22, 33]
print(T_mixed_nesting[2][1])