class human:
         def __init__(self, name, age): #this is a constructor
                  self.name = name
                  self.age = age

#ab banaate hain object:
person1 = human("sohom",22)
person2 = human("Riya",21)

print(person1.name)
print(person2.age)

class Employee: #this is how a class is written 
         language = 'python' #this is a class attribute
         salary = 1200000 # this is a class attribute 

harry = Employee()
harry.name = "Harry" # this is a object attribute
print(harry.name, harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.language, rohan.salary)

# here name is object attribute.
# salary and language are class attributes as they directly belong to the class.