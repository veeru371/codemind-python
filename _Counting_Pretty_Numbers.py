n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=0
    for i in range(a,b+1):
        t=i%10
        if t==2 or t==3 or t==9:
            c+=1
    print(c)
        