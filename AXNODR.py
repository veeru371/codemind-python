p=int(input())
for j in range(p):
    a=int(input())
    b=1
    for i in range(2,a+1):
        if i%2==0:
            b=b^i
        else:
            b=b&i
    print(b)