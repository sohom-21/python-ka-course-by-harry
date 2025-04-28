class Student:
         def __init__(self, name, roll, marks):
                  self.name = name
                  self.roll = roll
                  self.marks = marks
         
         def display(self):
                  print(f"Student Name : {self.name}")
                  print(f"Roll Number  : {self.roll}")
                  print(f"Marks        : {self.marks}")

class ManageStudents(Student):
         def add_students(self):
                  