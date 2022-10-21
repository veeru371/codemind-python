a=int(input())
b=list(map(int,input().split()))
c=0
t=[]
for i in b:
    for j in b:
        if i>j:
            c+=1
    t.append(c)
    c=0
print(*t)
    