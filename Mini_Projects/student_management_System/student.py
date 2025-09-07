from rich.console import Console
from rich.table import Table
console = Console()
class Student:

         def __init__(self, name, roll, marks):
                  self.name = name
                  self.roll = roll
                  self.marks = marks
         
         def display(self):
                  print(f"Student Name : {self.name}")
                  print(f"Roll Number  : {self.roll}")
                  print(f"Marks        : {self.marks}")
                  print("\n")
         
         def tabular_view(self):
                 table = Table(title = "student Details")
                 table.add_column("field", justify = "center", style = "cyan", no_wrap = True)
                 table.add_column("value", justify = "center", style = "magenta")
                 table.add_row("Name", self.name)
                 table.add_row("Roll", str(self.roll))
                 table.add_row("Marks", str(self.marks))
                 console.print(table)

class ManageStudents(Student):
         def add_students(self):
                  pass
         def remove_students(self):
                  pass
         def update_students(self):
                  pass
         def view_students(self):
                  pass