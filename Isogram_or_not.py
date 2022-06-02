n=input()
f=False
h=[]
for i in n:
    if i!=" ":
        if(n.count(i)>1):
            h.append(i)
if len(h)==0:
    print("True")
else:
    print("False")