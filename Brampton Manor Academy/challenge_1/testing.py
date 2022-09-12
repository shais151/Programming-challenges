import unittest

from rodConversions import *

class MyFirstTests(unittest.TestCase):

    def test_rodToMeter(self):
        self.assertEqual(rods_to_meters(10), 50.292)
    def test_rodToFurlong(self):
        self.assertEqual(rods_to_furlongs(10), 0.25)
    def test_meterToMile(self):
        self.assertEqual(meters_to_miles(10), 0.03125007767159208)
    def test_meterToFeet(self):
        self.assertEqual(meters_to_feet(10), 165.0)
    def test_speed(self):
        self.assertEqual(time_to_walk(10), 0.6048402129985564)
                         
if __name__ == '__main__':
    unittest.main()
