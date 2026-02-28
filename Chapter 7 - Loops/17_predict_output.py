l=[10,16,17,18,9,15,21,13]
for x in l:
    if (x%5==0):
        continue
    if(x%7==0):
        break
    print(x)
print("bye") #without completing the whole loop the interpreter wont reach here
