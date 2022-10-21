a=int(input())
b=list(map(int,input().split()))
c=int(input())
d=list(map(int,input().split()))
cnt=0
for i in range(len(b)):
    if b[i] in d:
        cnt+=1
if cnt==len(d):
    print("True")
else:
    print("False")