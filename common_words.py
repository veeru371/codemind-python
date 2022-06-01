a=input()
b=input()
n=a.lower()
m=b.lower()
n=n.split()
m=m.split()
h=[]
for i in range(len(m)):
    if m[i] in n:
        h.append(m[i])
        n.remove(m[i])
print(*h)