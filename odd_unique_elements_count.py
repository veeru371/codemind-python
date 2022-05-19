n=int(input())
t=list(map(int,input().split()))
f=[]
g=[]
count=0
for i in range(len(t)):
    if t[i]%2:
        f.append(t[i])
for j in f:
    if j not in g:
        g.append(j)
print(len(g))
        