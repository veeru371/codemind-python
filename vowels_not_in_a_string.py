n=input()
k=n
f=False
g=["a","e","i","o","u"]
for i in range(len(k)):
    if k[i] in g:
        g.remove(k[i])
if len(g)==0:
    print(0)
else:
    print(*g)