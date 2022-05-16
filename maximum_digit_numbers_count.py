n=int(input())
r=0
p=[]
count=0
count2=0
t=list(map(int,input().split()))
for i in range(len(t)):
    v=abs(t[i])
    while True:
        k=v%10
        v=v//10
        r=r+k
        count+=1
        if v==0:
            break
    p.append(count)
    count=0
mx=max(p)
for j in range(len(t)):
    if mx==p[j]:
        print(t[j],end=" ")