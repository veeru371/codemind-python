n=input()
count=0
j=[]
for i in n:
    if(n.count(i)==1):
        j.append(i)
        break
if len(j)==0:
    print(-1)
else:
    print(*j)

