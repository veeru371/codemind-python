n,m=map(int,input().split())
t=list(map(int,input().split()))
b=list(map(int,input().split()))
g=[]
v=[]
for i in range(len(t)):
    if t[i] in b:
        g.append(t[i])
for j in g:
    if j not in v:
        v.append(j)
print(*v)
