N=int(input())
q=[]
t=list(map(int,input().split()))
r,y=map(int,input().split())
a=min(r,y)
b=max(r,y)
for i in range(len(t)):
    if t[i]>=a and t[i]<=b:
        q.append(t[i])
if len(q)==0:
    print(-1)
else:
    print(*q)