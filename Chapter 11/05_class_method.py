class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The name of class attribute is {cls.a}")

e = employee()
e.o = 45
e.show()
        