b=int(input())
for i in range(b):
    a=input()
    t=int(a,8)
    g=bin(t).replace("0b"," ")
    print(int(g))
