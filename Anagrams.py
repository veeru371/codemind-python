n=input()
m=input()
t=n.lower()
r=m.lower()
g=sorted(t)
h=sorted(r)
if g==h:
    print("True")
else:
    print("False")