n=int(input())
m=list(map(int,input().split()))
t=[]
j=0
k=1
for i in range(len(m)):
    if (m[i]%2==0):
        t.insert(j,m[i])
        j+=2
    else:
        t.insert(k,m[i])
        k+=2
if len(m)%2!=0:
    t.append(0)
print(*t)