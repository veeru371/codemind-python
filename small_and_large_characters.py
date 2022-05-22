a=input()
b=a.split()
e=[]
r=[]
for i in range(len(b)):
    c=sorted(b[i])
    d=''.join(c)
    e.append(d)
for j in range(len(e)):
    q=e[j][0]
    w=e[j][-1]
    r.append(q)
    r.append(w)
print(*r)