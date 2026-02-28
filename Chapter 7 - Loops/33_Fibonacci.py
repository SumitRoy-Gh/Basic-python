n=int(input("enter a number: "))
a=0
b=1
print(a,end=" ")
for x in range(n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")