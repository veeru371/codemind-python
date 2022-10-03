a=int(input())
c=0
cnt=0
for i in range(2,a):
    if a%i==0:
        break
else:
    c+=1
r=str(a)
r=r[::-1]
p=int(r)
for j in range(2,p):
    if p%j==0:
        break
else:
    cnt+=1
d=c+cnt
if d==2:
    print("circular prime")
elif d==1:
    print("prime but not a circular prime")
else:
    print("not prime")