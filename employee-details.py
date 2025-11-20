class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Department: {self.department}, Salary: {self.salary}")

    def update_salary(self, department, increment):
        if self.department == department:
            self.salary += increment


employees = [
    Employee("kamakshi", 101, "HR", 30000),
    Employee("kadambari", 102, "IT", 40000),
    Employee("srikari", 103, "IT", 45000),
    Employee("vishalakshi", 104, "Finance", 35000)
]

print("Before Salary Update:")
for emp in employees:
    emp.display()

dept_name = "IT"
increment_amt = 5000

for emp in employees:
    emp.update_salary(dept_name, increment_amt)

print("\nAfter Salary Update:")
for emp in employees:
    emp.display()
