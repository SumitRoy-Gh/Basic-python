a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
max=max(a,b)
for x in range(max,a*b):
    if(max%a==0 and max%b==0):
        break
    max+=1
print(f"LCM is {max}") 