import unittest

from windChill import *

class MyFirstTests(unittest.TestCase):

    def test_one(self):
        self.assertEqual(calculate_chill(10,15), -6.5895344209562525)
    def test_two(self):
        self.assertEqual(calculate_chill(0,25), -24.093780999553864)
    def test_three(self):
        self.assertEqual(calculate_chill(-10,35), -41.16894662953316)
        
if __name__ == '__main__':
    unittest.main()
