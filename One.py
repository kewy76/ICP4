# Kate Williams
# 6/14/2018


class Employee:  # Employee class
    """A class representing an employee"""
    empNum = 2

    def increment(self):
        self.__class__.empNum += 1

    def __init__(self, n, f, s, d):
        self.name = n
        self.family = f
        self.salary = s
        self.dept = d

    def get_name(self):
        print("The employee's name is " + self.name)
        return

    def get_family(self):
        print("The employee's family name is " + self.family)
        return

    def get_salary(self):
        print("The employee's salary is " + str(self.salary))
        return

    def get_salary_value(self):  # Second salary function; only returns number
        return self.salary

    def get_dept(self):
        print("The employee's department is " + self.dept)
        return

    def get_emp_num(self):
        print("The number of employees is " + str(self.empNum))
        return


class FullTimeEmployee(Employee):
    """A class representing a full time employee
    Class inherits from employee"""
    def __init__(self, n, f, s, d, h):
        Employee.__init__(self, n, f, s, d)
        self.hours = h

    def get_hours(self):  # New type of data for new class; not inherited
        print("The employee works " + self.hours + " hours")


def avg_salary():  # Definition to average salary
    x = 0  # Define counter variable
    total = 0  # Define final answer variable
    while x < len(eArray):  # While the counter is in the # of employees
        total += eArray[x].get_salary_value()  # Add salary to total
        x += 1  # Iterate
    total = total / x  # Divide total salaries by # of employees
    print("The average salary is $" + str(total))


# Make some employees and call functions
Emp1 = Employee("Diana", "Prince", 4000, "Management")
Emp2 = FullTimeEmployee("Natasha", "Romanov", 3000, "Sales", "20")

eArray = [Emp1, Emp2]

print("For employee 1: ")
Emp1.get_name()
Emp1.get_family()
Emp1.get_salary()
Emp1.get_dept()
print("\n")

print("For employee 2: ")
Emp2.get_name()
Emp2.get_family()
Emp2.get_salary()
Emp2.get_dept()
Emp2.get_hours()
print("\n")

Emp1.get_emp_num()

avg_salary()