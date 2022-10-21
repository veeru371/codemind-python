a=int(input())
b=list(map(int,input().split()))
dic={}
t=[]
for i in b:
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
    print(max(t))