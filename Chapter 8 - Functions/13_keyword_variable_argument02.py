def printdetails(id,**details):
    print(f"details of {id}:")
    for d,v in details.items():
        print(f"{d} is {v}")
printdetails(id=101,name="abc",price=200)
print()
printdetails(id=200,name="sumit",price=500)