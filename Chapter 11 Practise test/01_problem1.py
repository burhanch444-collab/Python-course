class twoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(Self):
        print(f"The vector is {Self.i}i + {Self.j}j")

class threeDVector(twoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(Self):
     print(f"The vector is {Self.i}i + {Self.j}j + {Self.k}k")

a = twoDVector(1, 2)
a.show()
b = threeDVector(1, 2, 3)
b.show()
