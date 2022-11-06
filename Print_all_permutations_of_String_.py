from itertools import permutations
a=input()
t=[]
words = [''.join(p) for p in permutations(a)]
for i in words:
    print(i)