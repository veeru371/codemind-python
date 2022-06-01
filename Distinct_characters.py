g=input()
n=g.lower()
c=0
u=[]
b=[]
for i in n:
    if i!=" ":
        if(n.count(i)==1):
            b.append(i)
t=sorted(b)
print(''.join(t))