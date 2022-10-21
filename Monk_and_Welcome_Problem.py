a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
t=[]
for i in range(len(b)):
    y=b[i]+c[i]
    t.append(y)
print(*t)