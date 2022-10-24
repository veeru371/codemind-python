a=int(input())
t=[]
b=1000
for i in range(1,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            t.append(i)
            if i>a:
                break
r=t[-1]
n=t[-2]
if a in t:
    print(0)
else:
   h=(abs(a-r))
   q=(abs(a-n))
   print(min(h,q))