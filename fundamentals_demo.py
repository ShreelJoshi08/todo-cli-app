# Data Types
name = "Shreel"
age = 20
height = 5.9
is_intern = True
skills = ["Python", "Git", "VS Code"]

# Loop
for skill in skills:
    print("Skill:", skill)

# Function
def greet(user):
    return f"Hello, {user}!"

print(greet(name))

# Class & Object
class Intern:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain

    def show(self):
        print(f"{self.name} is learning {self.domain} at Agevole.")

intern1 = Intern("Shreel", "Python")
intern1.show()

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Execution completed.")