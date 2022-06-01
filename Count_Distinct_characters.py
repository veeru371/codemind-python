n=input()
t=[]
g=n.lower()
for i in g:
    if i!=" ":
        if i not in t:
            t.append(i)
print(len(t))
