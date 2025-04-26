class Student:
         def __init__(self, name, roll, marks):
                  self.name = name
                  self.roll = roll
                  self.marks = marks
         
         def display(self):
                  print(f' The name of the student is {self.name}, \n his/her roll is {self.roll}, \n marks obtained is {self.marks}')

student_list = []
for i in range(0,3):
         name = input("Enter the name of the student: ")
         roll = int(input("Enter roll: "))
         marks = int(input("Enter Marks: "))
         student = Student(name, roll, marks)
         student.display()
         dict_student = {
                  "name":student.name,
                  "roll":student.roll,
                  "marks": student.marks
         }
         student_list.append(dict_student.copy())
print(student_list)