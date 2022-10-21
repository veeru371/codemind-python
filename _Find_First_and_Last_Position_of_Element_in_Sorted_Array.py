a=int(input())
b=list(map(int,input().split()))
c=int(input())
t=[]
if c not in b:
    print(-1,-1)
else:
    for i in range(len(b)):
        if b[i]==c:
            t.append(i)
print(t[0],t[-1])
            
    