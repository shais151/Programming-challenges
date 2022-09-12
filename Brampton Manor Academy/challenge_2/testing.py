import unittest

from richter import *


class MyFirstTests(unittest.TestCase):

    def test_energy(self):
        self.assertEqual(richter_to_energy(3.4), 7943282347.242789)
    def test_tnt(self):
        self.assertEqual(energy_to_tnt(3.4), 1.8984900447521007)
        
if __name__ == '__main__':
    unittest.main()
