a=input()
b=input()
n=a.lower()
m=b.lower()
t=[]
u=[]
for i in n:
    if i!=" ":
        if i not in m:
            t.append(i)
for j in m:
    if j!=" ":
        if j not in n:
            t.append(j)
for h in t:
    if h not in u:
        u.append(h)
r=sorted(u)
print(''.join(r))
