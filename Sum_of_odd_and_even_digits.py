a=int(input())
b=list(map(int,input().split()))
ev=0
od=0
for i in range(len(b)):
    if i%2==0:
        ev+=b[i]
    else:
        od+=b[i]
y=ev-od
if y==0:
    print("YES")
else:
    print("NO")
