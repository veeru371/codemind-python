a=int(input())
b=list(map(int,input().split()))
t=b[::-1]
q=sorted(t)
if t==q:
    print("yes")
else:
    print("no")