n = int(input())
for x in range(n):
    if(x==0 or x==n-1):
        for y in range(n):
            print("*",end=" ")
        print()
    else:
        print("*"+" "*(2*n-3)+"*")