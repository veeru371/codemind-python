a=int(input())
for i in range(a):
    c,d=map(int,input().split())
    b=list(map(int,input().split()))
    for i in range(d):
        b.insert(0,b[-1])
        b.pop(-1)
    print(*b)