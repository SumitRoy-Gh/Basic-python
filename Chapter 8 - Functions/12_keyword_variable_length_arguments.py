def printdetails(**details):
    for d,v in details.items():
        print(f"{d} is {v}")
printdetails(id=101,name='abc',price=100)
print()
printdetails(id=102,name='sumit',price=200)