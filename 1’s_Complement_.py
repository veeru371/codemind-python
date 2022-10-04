a=int(input())
r=bin(a).replace("0b","")
t=[]
s=0
for i in r:
    t.append(i)
for j in range(len(t)):
    if t[j]=='1':
        t[j]='0'
    else:
        t[j]='1'
q=("".join(t))
q=q[::-1]
x=0
for p in q:
    if p=='1':
        s+=pow(2,x)
        x+=1
    else:
        x+=1
print(s)