a=int(input())
b=list(map(int,input().split()))
t=[]
for i in b:
    y=(i*i)
    t.append(y)
r=sorted(t)
print(*r)