class Employee: #this is how a class is written 
         language = 'python' #this is a class attribute
         salary = 1200000 # this is a class attribute 

# Instance attributes that belong to an instance (object). Assuming the class from the previous example 
harry = Employee()
harry.language = "JavaScript" # this is a object attribute
print(harry.language, harry.salary)

"""Note that instance attributes, take preference over class attributes during assignments & retrieval"""
"""
The attribute is first looked up:
1. is attribute present in object
2. is attribute present in class
## during printing or preforming operations 1 > precedence than 2
"""