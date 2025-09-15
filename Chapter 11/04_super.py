class employee:
    def __init__(self):
        print("Counstructor of employee")
    a = 1

class programmer(employee):
    def __init__(self):
        print("Counstructor of programmer")
    b = 2

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("Counstructor of manager")
    c = 3


# o = employee()
# print(o.a) # prints the  a attribute


o = programmer()
print(o.a, o.b) 

o = manager()
print(o.a, o.b, o.c)