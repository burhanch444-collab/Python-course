class employee:
    language = "python" # This is a class attribute.
    salary = 1200000

    def getinfo(self):
        print(f"The language is {self.language},The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")
Burhan = employee()
Burhan.language = "Java script" # This is an instance attribute.
print( Burhan.language,Burhan.salary)   

Burhan.getinfo()
Burhan.greet()
# employee.getinfo(Burhan)