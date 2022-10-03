n,m=map(int,input().split())
x=[]
y=[]
z=[]
for i in range(n):
    x.append(list(map(int,input().split())))
for i in range(len(x)):
    y.append(sum(x[i]))
print(sum(y))