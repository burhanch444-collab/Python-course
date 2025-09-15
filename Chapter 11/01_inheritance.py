class employee:
    company = "Microsoft"
    def show(self):
        print(f"Name of employee is: {self.name} and the salary is: {self.salary}")

# class programmer:
#     company = "Microsoft infotech"
#     def show(self):
#         print(f"Name of programmer is: {self.name} and the salary is: {self.salary}")
#     def language(self):
#         print(f"The name is: {self.name} and he is good at {self.language}")

class programmer(employee):
    company = "Microsoft infotech"
    def showlanguage(self):
        print(f"The name is: {self.name} and he is good at {self.language} language")

a = employee()
b = programmer()
print(a.company, b.company)  
        
