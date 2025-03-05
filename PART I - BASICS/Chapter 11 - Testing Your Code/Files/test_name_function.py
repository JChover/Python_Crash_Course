# A Passing Test - test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for name_function.py"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
