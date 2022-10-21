a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
t=[]
for i in range(len(b)):
    t.insert(d[i],b[i])
print(*t)