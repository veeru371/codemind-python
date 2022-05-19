n=int(input())
t=list(map(int,input().split()))
g=[]
for i in range(len(t)):
    if t[i] not in g:
        g.append(t[i])
        v=t.count(t[i])
        print(t[i],v,end=" ")