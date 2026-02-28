def fun(x):
    print(id(x))
    x=15
    print(id(x))
x=10
fun(x)
print(id(x))

def fun(l):
    print(id(l))
    l.append(15)
    print(id(l))
l=[10,20,30]
fun(l)
print(id(l))
#here ids will come same of the three because we are not changing the lists we are just modifying the existing lists locally.
