class Employee: #this is how a class is written 
         language = 'python' #this is a class attribute
         salary = 1200000 # this is a class attribute 
         def getInfo(self):
                  print(f"the language is {self.language}. The salary is {self.salary}")
         def greet(self):
                  print("Good morning")

# Instance attributes that belong to an instance (object). Assuming the class from the previous example 
harry = Employee()
harry.language = "JavaScript" # this is a object attribute
print(harry.language, harry.salary)
harry.getInfo()
# Employee.getInfo(harry)
harry.greet()
# Employee.greet(harry)
