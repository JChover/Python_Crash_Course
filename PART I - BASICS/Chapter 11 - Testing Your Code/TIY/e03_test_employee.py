# 11-3 Employee - e03_test_employee.py
import unittest
from e03_employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('John', 'Doe', 50000)

    def test_give_default_rise(self):
        self.employee.give_rise()
        self.assertEqual(self.employee.salary, 55000)

    def test_give_custom_rise(self):
        self.employee.give_rise(amount=10000)
        self.assertEqual(self.employee.salary, 60000)
