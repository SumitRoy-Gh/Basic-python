n=int(input("Enter sn number: "))
sum=1
for x in range(2,n):
    if(n%x==0):
        sum=sum+x
if(sum==n):
    print("It is a perfect number.")
else:
    print("It is not a perfect number.")

    