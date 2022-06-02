a=input()
b=input()
c=a.lower()
d=b.lower()
n=c.split()
m=d.split()
h=[]
for i in range(len(n)):
    if n[i] in m:
        h.append(n[i])
print(len(h))