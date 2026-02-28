def findfirst(n):
    while(n>=10):
        n=n//10
    return n
n=int(input("Enter a number: "))
print(findfirst(n))
