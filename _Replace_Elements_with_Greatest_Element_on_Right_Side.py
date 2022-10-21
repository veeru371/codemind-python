a=int(input())
b=list(map(int,input().split()))
t=[]
c=b[::-1]
r=0
for i in range(len(c)):
    if c[i]>=r:
        r=c[i]
        t.append(r)
    else:
        t.append(r)
t.pop(-1)
t.insert(0,-1)
w=t[::-1]
print(*w)
    