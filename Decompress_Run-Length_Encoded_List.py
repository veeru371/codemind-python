a=int(input())
b=list(map(int,input().split()))
t=[]
y=[]
p=0
q=[]
for i in range(len(b)):
    if i%2!=0:
        t.append(b[i])
    else:
        y.append(b[i])
for j in y:
    for k in range(j):
        q.append(t[p])
    p+=1
print(*q)