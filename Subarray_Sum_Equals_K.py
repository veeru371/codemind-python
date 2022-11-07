a,b=map(int,input().split())
c=list(map(int,input().split()))
d=len(c)
cnt=0
for i in range(d):
    summ=0
    for j in range(i,d):
        summ+=c[j]
        if summ==b:
            cnt+=1
print(cnt)
    