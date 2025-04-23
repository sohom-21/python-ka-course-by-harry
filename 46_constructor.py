class Employee:
         language = "python"
         salary = 1200000
         def __init__(self, name, salary, language): # this is called dunder method which is automatically called
         
         # The output is because of the order of arguments you passed when creating the Employee object:
         
         # So, "harry" goes to name, 1300000 goes to salary, and "JavaScript" goes to language.

                  self.name = name
                  self.language = language
                  self.salary = salary
                  print("I am creating an object")
         
         def getInfo(self):
                  print(f"The language is {self.language}. The salary is {self.salary}")
         
         @staticmethod
         def greet():
                  print("Good morning")
         
harry = Employee("harry", 1300000, "JavaScript")
# harry.name = "harry"
print(harry.name, harry.salary, harry.language)