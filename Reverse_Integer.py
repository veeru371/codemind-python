N=int(input())
rev=0
f=True
if N<0:
    N=N*(-1)
    f=False
while N>0:
    k=N%10
    N=N//10
    rev=(rev*10)+k
if f==False:
    print(rev*(-1))
else:
    print(rev)