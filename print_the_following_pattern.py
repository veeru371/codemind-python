a=int(input())
t=[]
while a:
    for i in range(1,a+1):
        r=str(i)
        t.append(r)
    print("".join(t))
    t.clear()
    a-=1
