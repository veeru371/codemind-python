a=input()
dic={}
cnt=0
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k,v in  dic.items():
    if v%2!=0:
        cnt+=1
if cnt>=2:
    print("Not Valid")
else:
    print("Valid String")