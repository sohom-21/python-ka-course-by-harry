class Student:
         def __init__(self, name, roll, marks):
                  self.name = name
                  self.roll = roll
                  self.marks = marks
         
         def display(self):
                  print(f' The name of the student is {self.name}, \n his/her roll is {self.roll}, \n marks obtained is {self.marks}')


sohom = Student('Sohom', 21, 87)

sohom.display()