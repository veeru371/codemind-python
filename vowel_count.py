n=input()
v=n
count=0
g=['a','e','i','o','u','A','E','I','O','U']
for i in range(len(n)):
    if n[i] in g:
        count+=1
if len(g)==0:
    print(0)
else:
    print(count)
    