import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_infix_to_list(self):
        calculate = Calculator()
        calculate.set_infix("(21 +1+.5 )/1.5")
        calculate.infix_to_list()
        self.assertEqual(calculate.get_infix_list, ["(", "21", "+", "1", "+", ".5", ")", "/", "1.5"])

    def test_infix_to_postfix_list(self):
        calculate = Calculator()
        calculate.set_infix("(12 + 2) * 4 - 3 / 2")
        calculate.infix_to_list()
        calculate.infix_to_postfix_list()
        self.assertEqual(calculate.get_postfix, [12.0, 2.0, "+", 4.0, "*", 3.0, 2.0, "/", "-"])

    def test_postfix_calculate(self):
        calculate = Calculator()
        calculate.set_infix("(1 + 2) * 4 + 3")
        calculate.infix_to_list()
        calculate.infix_to_postfix_list()
        calculate.postfix_calculate()
        self.assertEqual(calculate.get_result, 15.0)


if __name__ == '__main__':
    unittest.main()
