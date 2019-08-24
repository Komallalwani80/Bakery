import unittest
from bakery_solution.src.main.python.bakeryService import *


class TestProcessOrder(unittest.TestCase):
    """Basic test cases."""

    #This test case should pass
    def test_getMinPacks(self):
        availablePacks=[9,5,3]
        qty=13
        result={'2': '5', '1': '3'}
        self.assertEqual(getMinPacks(availablePacks,qty), result)

    def test_getBill(self):
        packs = {"VS5": [5, 3], "MB11": [8, 5, 2], "CF": [9, 5, 3]}
        price = {"VS5": {'5': '8.99', '3': '6.99'}, "MB11": {'8': '24.95', '5': '16.95', '2': '9.95'},
                 "CF": {'9': '16.99', '5': '9.95', '3': '5.95'}}
        x={'2': '5', '1': '3'}
        pCode = "CF"
        totalQuant = 13
        result = "13 CF $25.849999999999998\n \t2 X 5 $9.95\n\t1 X 3 $5.95"
        self.assertEqual(getBill(packs, price, x, pCode, totalQuant), result)


    # This test will fail because qty 1 is not available.
    def test_getMinPacks1(self):
        availablePacks = [9, 5, 3]
        qty = 1
        result = {'2': '5', '1': '3'}
        self.assertEqual(getMinPacks(availablePacks, qty), result)


if __name__ == '__main__':
    unittest.main()
