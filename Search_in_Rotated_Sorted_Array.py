a=int(input())
b=list(map(int,input().split()))
c=int(input())
if c not in b:
    print(-1)
else:
    for i in range(len(b)):
        if b[i]==c:
            print(i)