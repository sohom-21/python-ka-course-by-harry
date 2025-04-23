class Student:
         def __init__(self, name, roll, marks):
                  self.name = name
                  self.roll = roll
                  self.marks = marks
         
         def display(self):
                  print(f' The name of the student is {self.name}, \n his/her roll is {self.roll}, \n marks obtained is {self.marks}')

for i in range(0,3):
         name = input("Enter the name of the student: ")
         roll = int(input("Enter roll: "))
         marks = int(input("Enter Marks: "))
         student = Student(name, roll, marks)
         data = student.display()
         print(type(data))