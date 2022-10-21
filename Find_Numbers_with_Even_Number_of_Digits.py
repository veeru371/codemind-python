a=int(input())
b=list(map(int,input().split()))
c=0
for i in b:
    r=str(i)
    q=len(r)
    if q%2==0:
        c+=1
print(c)