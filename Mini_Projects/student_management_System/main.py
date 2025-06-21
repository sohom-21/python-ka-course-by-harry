from student import Student
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static

def main():
         s1 = Student("John Doe", "12345", 85)
         s2 = Student("Jane Smith", "67890", 90)
         # s1.display()
         # s2.display()
         s1.tabular_view()
         s2.tabular_view()
         

if __name__ == "__main__":
         main()