N=int(input())
s=0
t=list(map(int,input().split()))
r,y=map(int,input().split())
a=min(r,y)
b=max(r,y)
for i in range(len(t)):
    if t[i]>=a and t[i]<=b:
        s=s+t[i]
print(s)