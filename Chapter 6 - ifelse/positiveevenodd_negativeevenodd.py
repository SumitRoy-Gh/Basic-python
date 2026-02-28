n=int(input("Enter a number: "))
if(n>0):
    if(n%2==0):
        print("Positive even")
    else:
        print("Positive odd")
if(n<0):
    if(n%2==0):
        print("Negative even")
    else:
        print("Negative odd")

'''another approach
if(n>0):
    print("positive",end=" ")
    if(n%2==0):
        print("even")
    else:
        print("odd")'''