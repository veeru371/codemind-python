a=int(input())
for i in range(a):
    c=0
    b=input()
    j=1
    for k in range(len(b)):
        if j==len(b):
            break
        if b[k]==b[j]:
            c+=1
            j+=1
        else:
            j+=1
    print(c)