a=input()
b=("aeiou")
t=[]
r=[]
for i in a:
    if i in b:
        t.append("V")
    else:
        t.append("C")
d=[0]
for j in range(len(t)):
    if d[-1]!=t[j]:
        d.append(t[j])
for p in d:
    if p!=0:
        r.append(p)
print("".join(r))
    