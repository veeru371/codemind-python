n=input()
m=input()
for i in range(len(n)):
    if m in n[i]:
        print(True)
        print(i)
        break
else:
    print("False")