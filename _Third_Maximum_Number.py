a=int(input())
b=list(map(int,input().split()))
q=set(b)
v=sorted(q)
if len(v)==1:
    print(v[0])
if len(v)==2:
    print(v[1])
if len(v)>=3:
    print(v[-3])