a=input()
b=("0123456789")
s=0
for i in range(len(a)):
    if a[i] in b:
        t=int(a[i])
        s=s+t
print(s)