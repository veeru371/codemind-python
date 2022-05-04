n=int(input())
s=0
k=list(map(int,input().split()))
t=[]
for i in k:
    if i not in t:
        t.append(i)
        
for j in range(len(t)):
    if t[j]%2:
        s=s+t[j]
print(s)