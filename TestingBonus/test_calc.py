# Meg Veitz
# 4/14/21

import unittest
from . import calc


class TestCalc(unittest.TestCase):
    def test_calculate_teir3_sales_10(self):
        tier = 3
        sales = 10_001
        bonus = sales * .15

        response = calc.calculate_bonus(tier, sales)

        self.assertEqual(response, bonus, "Should be a {} bonus".format(bonus))

    def test_calculate_teir3_sales_9(self):
        tier = 3
        sales = 9_500
        bonus = sales * .075

        response = calc.calculate_bonus(tier, sales)

        self.assertEqual(response, bonus, "Should be a {} bonus".format(bonus))

    def test_calculate_teir2_sales_10(self):
        tier = 2
        sales = 10_001
        bonus = sales * .10

        response = calc.calculate_bonus(tier, sales)

        self.assertEqual(response, bonus, "Should be a {} bonus".format(bonus))

    def test_calculate_teir2_sales_9(self):
        tier = 2
        sales = 9_500
        bonus = sales * .05

        response = calc.calculate_bonus(tier, sales)

        self.assertEqual(response, bonus, "Should be a {} bonus.".format(bonus))

    def test_calculate_teir1_sales_10(self):
        tier = 1
        sales = 10_001
        bonus = sales * .05

        response = calc.calculate_bonus(tier, sales)

        self.assertEqual(response, bonus, "Should be a {} bonus".format(bonus))


if __name__ == '__main__':
    unittest.main()
