a=int(input())
for i in range(a):
    b=int(input())
    c=0
    t=bin(b).replace("0b","")
    for i in t:
        if i=='1':
            c+=1
    print(c)