class Employee:
         company = 'ITC'
         name = 'Default name'
         def show(self):
                  print(f'The name is {self.name} and the salary is {self.company}')

class Programmer(Employee):
         company = 'ITC_Infotech'
         def showlanguage(self):
                  print(f'The name is{self.name} and he is good with {self.language} language')

a = Employee()
b = Programmer()
b.show()
print(a.company,b.company)