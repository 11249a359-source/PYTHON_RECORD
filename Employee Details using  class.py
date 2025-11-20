AIM:
To write a python program by creating a class called Employee to store the details of Name,
Employee_ID, Department and Salary, and implement a method to update salary of employees
belonging to a given department.

ALGORITHM:
1. Start
2. Define a class Employee with attributes:
a) name
b) emp_id
c) department
d) salary
3. Define the init () method to initialize these attributes.
4. Define a method update_salary_by_dept(self, percentage) inside the class to update the
salary based on the given percentage (optional: can be done externally too).
5. Create a list of Employee objects.
6. Accept department name and increment percentage from the user.
7. Traverse the list and for each employee:
a) If employee’s department matches the input department:
i) Update salary by applying the percentage increase.

8. Display updated employee details.
9. End

PROGRAM:

class Employee:
def init (self, name, emp_id, department, salary):
self.name = name
self.emp_id = emp_id
self.department = department
self.salary = salary

39 | P a g e

def display(self):
print(f&quot;Name: {self.name}, ID: {self.emp_id}, Dept: {self.department}, Salary:
{self.salary}&quot;)
def update_salary(self, percentage):
self.salary += self.salary * (percentage / 100)
employees = [
Employee(&quot;Alice&quot;, 101, &quot;HR&quot;, 50000),
Employee(&quot;Bob&quot;, 102, &quot;IT&quot;, 60000),
Employee(&quot;Charlie&quot;, 103, &quot;HR&quot;, 52000),
Employee(&quot;David&quot;, 104, &quot;Finance&quot;, 55000),
Employee(&quot;Eva&quot;, 105, &quot;IT&quot;, 58000)
]
dept = input(&quot;Enter department to update salary: &quot;)
percent = float(input(&quot;Enter salary increment percentage: &quot;))

print(&quot;\n--- Updated Employee Details ---&quot;)
for emp in employees:
if emp.department.lower() == dept.lower():
emp.update_salary(percent)
emp.display()

OUTPUT:
Enter department to update salary: HR
Enter salary increment percentage: 10

--- Updated Employee Details ---
Name: Alice, ID: 101, Dept: HR, Salary: 55000.0
Name: Bob, ID: 102, Dept: IT, Salary: 60000
Name: Charlie, ID: 103, Dept: HR, Salary: 57200.0
Name: David, ID: 104, Dept: Finance, Salary: 55000
Name: Eva, ID: 105, Dept: IT, Salary: 58000
