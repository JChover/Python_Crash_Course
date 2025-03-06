# 11-3 Employee - e03_employee.py
class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_rise(self, amount=5000):
        self.salary += amount
