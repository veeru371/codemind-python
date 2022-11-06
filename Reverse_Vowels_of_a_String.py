a=input()
a=list(a)
b=("aeiou")
c=("AEIOU")
t=[]
y=[]
for i in range(len(a)):
    if a[i] in b or a[i] in c:
        t.append(a[i])
    if a[i] in b or a[i] in c:
        y.append(i)
p=t[::-1]
for l in range(len(p)):
    a.pop(y[l])
    a.insert(y[l],p[l])
print("".join(a))