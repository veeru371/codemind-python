a=int(input())
b=list(map(int,input().split()))
c=int(input())
q=max(b)
t=[]
for i in b:
    r=(i+c)
    if r>=q:
        t.append("True")
    else:
        t.append("False")
print(*t)