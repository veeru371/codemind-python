n,m=map(int,input().split())
x=[]
y=[]
s=0
y=0
u=0
for i in range(n):
    x.append(list(map(int,input().split())))
for k in range(len(x)):
    print(sum(x[k]),end=" ")