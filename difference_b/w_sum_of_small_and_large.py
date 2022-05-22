a=input()
b=a.split()
e=[]
r=[]
t=[]
s=0
z=0
for i in range(len(b)):
    c=sorted(b[i])
    d=''.join(c)
    e.append(d)
for j in range(len(e)):
    q=e[j][0]
    w=e[j][-1]
    r.append(q)
    t.append(w)
for k in range(len(r)):
    s=s+(ord(r[k]))
for g in range(len(t)):
    z=z+(ord(t[g]))
print(abs(s-z))
    

