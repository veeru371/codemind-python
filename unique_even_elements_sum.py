n=int(input())
t=list(map(int,input().split()))
h=[]
k=[]
for i in range(len(t)):
    if t[i]%2==0:
        h.append(t[i])
for j in h:
    if j not in k:
        k.append(j)
g=sum(k)
print(g)