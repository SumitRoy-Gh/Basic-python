n=int(input("Enter a number: "))
#m=int(input("Enter a number: "))
for x in range(2,n):
    if(n%x==0):
        print(x)
        break