'''n=int(input("Enter a year: "))
if(n%4==0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")'''

'''this is wrong program.
Because there are some years which are divisible by 4 but they are not leap year.
years which divisible by 4 and not buy hundred are definitely leap year.
years which are divisible by 400 are definitely leap year.'''

n=int(input("Enter a year: "))
if(n%4==0)and(n%100!=0):
    print("It is a leap year.")
if(n%400==0):
    print("It is a leap year.")
else:
    print("It is not a leap year.")
