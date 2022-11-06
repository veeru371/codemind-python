a=int(input())
t=[]
c=0
for i in range(a):
    b=input()
    t.append(b)
for i in range(len(t)):
    if t[i]=="X++" or t[i]=="++X":
        c+=1
    else:
        c-=1
print(c)