class employee:
    company = "Microsoft"
    name = "Burhan"
    def show(self):
        print(f"Name of employee is {self.name} and the company is {self.company}")

class coder:
    language = "python"
    def printlanguages(self):
        print(f"out of all the languages here is your languages {self.language}")

class programmer(employee, coder):
    company = "Microsoft infotech"
    def showlanguage(self):
        print(f"The name is {self.company} and he is good at {self.language} language")

a = employee()
b = programmer()

b.show()
b.printlanguages()       
b.showlanguage()   