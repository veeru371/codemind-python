a=int(input())
if a<=2:
    print("The pattern is not possible")
else:
    for i in range(1,a+1):
        print(i*("*"))
        if i==a:
            t=a-1
            while t:
                print(t*("*"))
                t-=1
    