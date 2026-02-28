n=int(input("Enter a number: "))
count=1
for x in range(2,n+1):
    count=count*x
print(f"The factorial of {n} is {count}") 