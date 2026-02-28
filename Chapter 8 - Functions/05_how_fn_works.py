def fun2():
    print("Inside fun2()")
def fun1():
    print("before fun2()")
    fun2()
    print("After fun1()")
print("Before fun1()")
fun1()
print("After fun()")
