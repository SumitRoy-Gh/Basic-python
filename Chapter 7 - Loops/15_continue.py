n=int(input("Enter a number: "))
for x in range(n+1):
    if(x%5==0):
        continue
    print(x)