class Demo:
    a = 4

o = Demo() 
print(o.a) # print the class attribute because instance attribute is not persent
o.a = 0 # instance attribute is set
print(o.a) # print the instance attribute because instance attribute is persent
print(Demo.a) # print the class attribute
