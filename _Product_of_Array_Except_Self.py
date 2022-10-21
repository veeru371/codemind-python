a=int(input())
b=list(map(int,input().split()))
t=[]
y=1
for i in b:
    y=y*i
for j in b:
    g=(y//j)
    t.append(g)
print(*t)