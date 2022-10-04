a=int(input())
b=list(map(int,input().split()))
dic={}
for i in b:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in dic.items():
    if v==1:
        print(k)