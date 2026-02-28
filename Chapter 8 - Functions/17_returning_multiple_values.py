def addmultiply(x,y):
    sum=x+y
    multiplication=x*y
    return sum,multiplication
s,m=addmultiply(10,20)
print(s)
print(m)
#here we created a tuple and returned the value as a tuple.the two values got stored in the two variables


def addmultiply(x,y):
    sum=x+y
    multiplication=x*y
    return [sum,multiplication]
s,m=addmultiply(10,20)
print(s)
print(m)
#returning as a tuple
