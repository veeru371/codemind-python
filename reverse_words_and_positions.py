N=input()
r=N.split()
a=[]
for i in range(len(r)):
    g=r[i][::-1]
    a.append(g)
print(*a[::-1])