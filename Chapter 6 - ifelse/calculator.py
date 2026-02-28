import sys
print("""Enter an opration:
      1.Addition
      2.Substraction
      3.Multiplication""")
choice=int(input("Select your operation 1/2/3: "))
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if choice not in(1,2,3):
    print("Invalid input.")
    sys.exit()
if(choice==1):
    result=a+b
    print(result)
if(choice==2):
    result=a-b
    print(result)
if(choice==3):
    result=a*b
    print(result)

