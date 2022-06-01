g=input()
n=g.upper()
c=0
u=[]
for i in n:
    if i!=" ":
        if(n.count(i)==1):
            c+=1
print(c)