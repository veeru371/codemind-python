a=int(input())
for i in range(a):
    y=[]
    b=input()
    t=int(b,16)
    r=bin(t).replace("0b","")
    for i in r:
        y.append(i)
    while True:
        if len(y)%4==0:
            break
        else:
            y.insert(0,"0")
    print("".join(y))