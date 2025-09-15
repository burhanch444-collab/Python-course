class employee:
    language = "python" # This is a class attribute.
    salary = 1200000

    def __init__(self,name,salary,language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating a amazing project")

    def getinfo(self):
        print(f"The language is {self.language},The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")
Burhan = employee("Burhan", 1300000, "javascript")
# Burhan.name = "Burhan"
print( Burhan.name,Burhan.salary,Burhan.language)

# Usman = employee()
