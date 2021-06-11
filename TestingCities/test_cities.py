# Meg Veitz
# 4/14/21

import unittest
from . import city_functions


class TestPlace(unittest.TestCase):

    def test_combine_names(self):
        city = "Santiago"
        country = "Chile"
        response = "Santiago, Chile"
        combine_names = city_functions.combine_names(city, country)
        self.assertEqual(combine_names, response, "Should be Santiago, Chile")

    def test_combine_names_again(self):
        # inputs
        city = "Bismarck"
        country = "United States of America"
        bismark = "Bismarck, United States of America"

        # run the function
        combine_names = city_functions.combine_names(city, country)

        # make sure it is what we want
        self.assertEqual(combine_names, bismark, "Should be Bismarck, United States of America")


if __name__ == '__main__':
    unittest.main()
