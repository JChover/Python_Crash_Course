# A Passing Test - test_name_function.py
import unittest
from name_function_fixed import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for name_function_pass.py"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()

# Adding New Tests- test_name_function.py
import unittest
from name_function_fixed import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for name_function_pass.py"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name,  'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
