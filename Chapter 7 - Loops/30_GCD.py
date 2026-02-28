a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
small=min(a,b)
for x in range(1,small+1):
    if(a%x==0 and b%x==0):
       gcd=x 
print(f"gcd is {gcd}")