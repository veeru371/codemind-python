p=input()
b=("0123456789")
c=("abcdefghijklmnopqrstuvwxyz")
a=[]
cnt=0
p=p.lower()
for r in p:
    if r not in b and r not in c:
        cnt+=1
    if r in b:
        a.append(r)
t=[]
i=0
j=1
if cnt%2==0:
    for p in range(len(a)):
        v=int(a[p])
        if v%2==0:
            v=str(v)
            t.insert(i,v)
            i+=2
        else:
            v=str(v)
            t.insert(j,v)
            j+=2
    print("".join(t))
else:
    for p in range(len(a)):
        v=int(a[p])
        if v%2!=0:
            v=str(v)
            t.insert(i,v)
            i+=2
        else:
            v=str(v)
            t.insert(j,v)
            j+=2
    print("".join(t))
