n=int(input())
for i in range(n):
    b=int(input())
    c=list(map(int,input().split()))
    q=sorted(c)
    if c==q:
        print(0)
    else:
        y=(q[-1]-q[0])
        print(y)