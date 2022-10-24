b=int(input())
for i in range(b):
    a=int(input())
    t=[]
    b=1000
    for i in range(1,b+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                t.append(i)
                if i>a:
                    break
    y=t[-1]
    n=t[-2]
    q=abs(a-y)
    w=abs(a-n)
    if q==w:
      print(n)
    elif q<w:
        print(y)
    else:
        print(n)