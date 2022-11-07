a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
e=int(input())
cnt=0
for i in range(len(b)):
    if e>=b[i] and e<=d[i]:
        cnt+=1
print(cnt)