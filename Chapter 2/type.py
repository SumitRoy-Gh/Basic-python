a=30
t=type(a) #class <int>
print(t)

a=30.12
t=type(a) #class <float>
print(t)

a="30.12"
t=type(a) #class <string>
print(t)

a="30.12"
b=float(a) # a but the type hould be float
t=type(b)
print(t)

a="30.12"
#b=float(a) # a but the type hould be float
t=type(a)
print(t)

a="30"
b=int(a) # a but the type hould be float
t=type(b)
print(t)