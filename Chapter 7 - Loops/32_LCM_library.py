import math
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
gcd=math.gcd(a,b)
lcm=(a*b)/gcd
print("LCM is",lcm)