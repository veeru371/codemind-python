a=int(input())
b=list(map(int,input().split()))
c=int(input())
t=[]
for i in range(len(b)):
    if c==len(b):
        break
    if i==c:
        break
    t.append(b[i])
    t.append(b[c])
    c+=1
print(*t)