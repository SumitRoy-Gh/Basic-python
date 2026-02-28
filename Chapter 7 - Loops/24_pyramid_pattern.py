n=int(input("Enter a number: "))
for x in range(n):
    for y in range(n-x-1):
        print(" ",end=" ")
    for z in range(2*x+1):
        print("*",end=" ")
    print()