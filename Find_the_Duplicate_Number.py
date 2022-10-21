a=int(input())
b=list(map(int,input().split()))
for i in b:
    y=b.count(i)
    if y>1:
        n=i
print(n)