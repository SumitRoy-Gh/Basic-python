n=int(input("Enter a number: "))
original_num=n
reversed_num=0
while(n>0):
    digit=n%10
    reversed_num= reversed_num*10 + digit
    n=n//10
if(original_num==reversed_num):
    print("It is a palindrome.")
else:
    print("It is not a palindrome")