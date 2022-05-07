p,q,r=map(int,input().split())
t=(2*p*q*r*512)
KB=1024
g=t//KB
s1=str(g)
s2=str("KB")
print(s1+s2)