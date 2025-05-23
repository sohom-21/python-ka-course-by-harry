class Employee:
    company = 'ITC'

    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary

    def show(self):
        print(f'The name is {self.name} and the salary is {self.salary}')


class Programmer(Employee):
    company = "ITC InfoTech"

    def __init__(self, name, language, skill_level, salary=0):  # Add salary with a default value
        super().__init__(name, language, salary)  # Pass salary to the parent class
        self.skill = skill_level

    def show_language(self):
        print(f"The name is {self.name}, he is good with {self.language} language, and his skill level is {self.skill}")


# Creating objects
a = Employee("Sohom", "Python", 100000)
b = Programmer("Rohan", "Java", "Expert", 120000)  # Pass salary for Programmer

# Using methods
b.show_language()
print(a.company, b.company)