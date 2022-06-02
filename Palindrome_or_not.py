n=input()
h=[]
t=n.lower()
m=t.split()
for i in m:
    if i==i[::-1]:
        print("True")
    else:
        print("False")