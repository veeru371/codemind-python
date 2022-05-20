n=input()
f=[]
count=0
for i in range(len(n)):
    f.append(n[i])
for j in range(len(f)):
    if(f[j].isupper()):
        count+=1
print(count)
    

