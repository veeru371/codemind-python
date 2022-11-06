a=input()
dic={}
t=[]
r=[]
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    t.append(v)
q=set(t)
p=sorted(q)
if len(p)==1:
    print(-1)
else:
    w=p[-2]
    for k,v in dic.items():
        if w==v:
            r.append(k)
    print(r[0])