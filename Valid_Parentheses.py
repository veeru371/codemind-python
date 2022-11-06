q=int(input())
for j in range(q):
    a=input()
    t=[]
    r=0
    dic={")":"(","}":"{","]":"["}
    for i in a:
        if i in dic.values():
            t.append(i)
        elif t and dic[i]==t[-1]:
            t.pop()
        else:
            r+=1
   
    if len(t)==0:
        print("True")
    else:
        print("False")
    