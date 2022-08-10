m=int(input())
for i in range(m):
    n=int(input())
    i=0
    t=[]
    while n:
        g=n%10
        n=n//10
        if g!=0:
            b=pow(2,i)
            t.append(b)
            i+=1
        else:
            i+=1
    print(sum(t))
