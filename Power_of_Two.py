a=int(input())
i=0
t=[]
while True:
    q=pow(2,i)
    if q>a:
        break
    else:
        t.append(q)
        i+=1
if a in t:
    print("True")
else:
    print("False")