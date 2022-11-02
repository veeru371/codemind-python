a=input()
dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
c=dic[a[-1]]
for i in range(len(a)-1):
    if dic[a[i]]<dic[a[i+1]]:
        c-=dic[a[i]]
    else:
        c+=dic[a[i]]
print(c)