n,z=map(int,input().split())
r=0
count=0
count1=0
t=list(map(int,input().split()))
for i in range(len(t)):
    v=abs(t[i])
    while True:
        g=v%10
        v=v//10
        r=r+g
        count+=1
        if v==0:
            break
    if z==count:
        count1+=1
    count=0
print(count1)