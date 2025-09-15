
def greatest(a, b, c):
    if(a>b or a>c):
        return a
    elif(b>a or b>c):
        return b
    elif(c>b or c>a):
         return c
   
a = 1
b = 2
c = 3

print(greatest(a, b, c))    