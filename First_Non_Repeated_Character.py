a=int(input())
for i in range(a):
    t=[]
    dic={}
    b=int(input())
    c=input()
    y=[]
    for i in c:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for k,v in dic.items():
        if v==1:
            t.append(k)
    if len(t)==0:
        print(-1)
    else:
        for j in range(len(c)):
            for k in range(len(t)):
                if c[j]==t[k]:
                    y.append(c[j])
                    break
        print(y[0])