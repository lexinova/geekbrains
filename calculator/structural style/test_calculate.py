from unittest import TestCase
import calculate


class Test(TestCase):
    def test_infix_to_list(self):
        self.assertEqual(calculate.infix_to_list("(21 +1+.5 )/1.5"), ["(", "21", "+", "1", "+", ".5", ")", "/", "1.5"])

    def test_infix_to_postfix_list(self):
        postfix = calculate.infix_to_postfix_list("(12 + 2) * 4 - 3 / 2")
        self.assertEqual(postfix, [12.0, 2.0, "+", 4.0, "*", 3.0, 2.0, "/", "-"])

    def test_postfix_calculate(self):
        postfix = calculate.infix_to_postfix_list("(1 + 2) * 4 + 3")
        result = calculate.postfix_calculate(postfix)
        self.assertEqual(result, 15.0)
