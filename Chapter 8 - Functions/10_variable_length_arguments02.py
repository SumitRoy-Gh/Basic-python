def sum(int_sum,*elements):
    res=int_sum
    for x in elements:
        res=res+x
    return res
print(sum(0,10,20))
print(sum(5,10,15))