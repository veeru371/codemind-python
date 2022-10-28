a=int(input())
t=[]
y=[]
for i in range(1,a+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            t.append(i)
for p in t:
    for q in t:
        r=(p*q)
        if r==a:
            y.append(p)
            y.append(q)
if len(y)==0:
    print(-1)
else:
    print(y[0],y[1])