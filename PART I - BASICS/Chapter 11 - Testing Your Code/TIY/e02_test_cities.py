# 11-2 Population - e02_test_cities.py
import unittest
from e02_city_functions import get_formatted_places

class NamesTestCase(unittest.TestCase):
    """Test for name_function_pass.py"""

    def test_city_country(self):
        """Do places like 'Santiago, Chile' work?"""
        place = get_formatted_places('santiago', 'chile')
        self.assertEqual(place, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do places like 'Santiago, Chile - population 5000000' work?"""
        place = get_formatted_places('santiago', 'chile', population=5000000)
        self.assertEqual(place, 'Santiago, Chile - Population 5000000')

if __name__ == '__main__':
    unittest.main()
