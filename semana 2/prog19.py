from operator import attrgetter


class Employee():
    def _init_(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def _repr_(self):
        return '({},{},${})' .format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

# def e_sort(emp):
#   return emp.salary

s_employees = sorted(employees, key=attrgetter('age'))

print(s_employees)
