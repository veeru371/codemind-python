n=int(input())
a=0
b=1
if n==1:
    print(1)
else:
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
        vx=a
        if c>n:
            mx=c
            break
    p=abs(n-vx)
    q=abs(n-mx)
    if p<q:
        print(vx)
    elif p==q:
        print(vx,mx)
    else:
        print(mx)