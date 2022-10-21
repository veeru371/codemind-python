a=int(input())
b=list(map(int,input().split()))
t=[]
for i in range(1,a+1):
    if i not in b:
        t.append(i)
print(t[0])
    