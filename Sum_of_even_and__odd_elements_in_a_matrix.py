n,m=map(int,input().split())
x=[]
y=[]
z=[]
ev=0
od=0
for i in range(n):
    x.append(list(map(int,input().split())))
for i in range(len(x)):
    y=x[i]
    for j in range(len(y)):
        if y[j]%2==0:
            ev+=y[j]
        else:
            od+=y[j]
print(ev,od)
            