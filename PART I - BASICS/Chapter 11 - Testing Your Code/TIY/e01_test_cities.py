# City, Country - e01_test_cities.py
import unittest
from e02_city_functions import get_formatted_places

class NamesTestCase(unittest.TestCase):
    """Test for name_function_pass.py"""

    def test_city_country(self):
        """Do places like 'Santiago, Chile' work?"""
        place = get_formatted_places('santiago', 'chile')
        self.assertEqual(place, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
