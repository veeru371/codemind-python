a=input()
b=len(a)
t=[]
y=[]
p=0
q=-1
for i in range(0,b+1):
    t.append(i)
for j in a:
    if j=="I":
        y.append(t[p])
        p+=1
    else:
        y.append(t[q])
        q-=1
for h in t:
    if h not in y:
        y.append(h)
print(*y)
