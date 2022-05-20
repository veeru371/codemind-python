n=input()
v=n.split()
count=0
b=['a','e','i','o','u']
for i in range(len(v)):
    for j in v[i]:
        if j in b:
            count+=1
    print(count,end=" ")
    count=0

