# CHAPTER 10 - PRACTICE SET

# 1. Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company = 'Microsoft'
    def __init__(self,dev_name, jobtitle,salary_dev,dev_team):
        self.name = dev_name
        self.job_title = jobtitle
        self.salary = salary_dev
        self.team = dev_team

    def display(self):
        print(f'your company is {self.company}')
        print(f"your name is {self.name}")
        print(f"your jobTitle is {self.job_title}")
        print(f"your salary is {self.salary}")
        print(f"your team number is {self.team}")

employee_name = input("Enter your name: ")
employee_title = input("Enter your Job Title: ")
employee_salary = int(input("Enter your salary: "))
employee_team = input("Enter your team in format(team?): ")

employee = Programmer(employee_name,employee_title,employee_salary,employee_team)
employee.display()