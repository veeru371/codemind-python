n=input()
r=[]
b=[]
g=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(n)):
    if n[i] in g:
        r.append(n[i])
for i in r:
    if i not in b:
        b.append(i)
if len(b)==0:
    print(-1)
else:
    print(*b)