a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
for i in range(len(c)):
    if c[i] in d:
        d.remove(c[i])
if len(d)==0:
    print("Yes")
else:
    print("No")