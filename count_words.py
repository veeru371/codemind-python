n=input()
v=n.split()
g=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in range(len(v)):
    if ((v[i][0] in g) and (v[i][-1] not in g)):
        count+=1
print(count)