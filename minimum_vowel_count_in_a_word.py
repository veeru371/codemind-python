n=input()
v=n.split()
h=[]
count=0
b=['a','e','i','o','u']
for i in range(len(v)):
    for j in v[i]:
        if j in b:
            count+=1
    h.append(count)
    count=0
print(min(h))
