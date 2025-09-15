from functools import reduce
a = [11, 34, 624, 752, 25, 72, 63]

def greatest(a,b):
    if(a>b):
        return a
    return b

print(reduce(greatest, a))