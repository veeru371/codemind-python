n=int(input())
s=0
c=[]
g=[]
t=list(map(int,input().split()))
k=int(input())
for i in range(len(t)):
    if t[i] not in g:
        g.append(t[i])
        v=t.count(t[i])
        if k==v:
            c.append(t[i])
if len(c)==0:
    print("-1")
else:
    print(*c)