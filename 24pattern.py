n=int(input("Enter your number which need to print: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("@",end=" ")
    print()