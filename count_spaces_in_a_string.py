n=input()
h=[]
count=0
for i in range(len(n)):
    h.append(n[i])
for j in range(len(h)):
    if h[j]==(" "):
        count+=1
print(count)
    
    