import unittest

from calculator import *

class MyFirstTests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(check_values("1 2 +"), [1, 2, "+"])

    def test_subtract(self):
        self.assertEqual(check_values("3 1 -"), [3, 1, "-"])

    def test_multiply(self):
        self.assertEqual(check_values("6 5 *"), [6, 5, "*"])

    def test_divide(self):
        self.assertEqual(check_values("90 10 /"), [90, 10, "/"])

    def test_division_integer(self):
        self.assertEqual(check_values("10 7 //"), [10, 7, "//"])
    
    def test_division_modulo(self):
        self.assertEqual(check_values("10 7 %"), [10, 7, "%"])

    def test_power(self):
        self.assertEqual(check_values("5 2 **"), [5, 2, "**"])

    def test_float_input(self):
        self.assertEqual(check_values("5.3 2.2 +"), [5.3, 2.2, "+"])
    
    def test_divison_zero(self):
        self.assertEqual(check_values("10 0 /"), -1)
    
    def test_invalid_args(self):
        self.assertEqual(check_values("a b c"), -1)

    # def test_quit(self):
    #     self.assertEqual(check_values("q"), quit())
                         
if __name__ == '__main__':
    unittest.main()
