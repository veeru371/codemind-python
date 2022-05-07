N=int(input())
f=False
t=list(map(int,input().split()))
for i in range(len(t)):
    if t[i]==1 or t[i]==0:
        f=True
    else:
        f=False
if f==True:
    print("True")
else:
    print("False")