import unittest

from cardCheckSum import *

class MyFirstTests(unittest.TestCase):

    def test_PAN_1(self):
        self.assertEqual(identifyPAN(str(4111111111111111)), 111111111)

    def test_PAN_2(self):
        self.assertEqual(identifyPAN(str(5555555555554444)), 555555444)

    def test_checkSum_1(self):
        self.assertEqual(identifyChecksum(str(4111111111111111)), 1)

    def test_checkSum_2(self):
        self.assertEqual(identifyChecksum(str(5555555555554444)), 4)

    def test_issuer_1(self):
        self.assertEqual(identifyIssuer(str(4111111111111111)), "Visa")
    
    def test_issuer_2(self):
        self.assertEqual(identifyIssuer(str(5555555555554444)), "MasterCard")

    def test_validity_1(self):
        self.assertEqual(checkValidity(4111111111111111, 1), "valid")

    def test_validity_2(self):
        self.assertEqual(checkValidity(5555555555554444, 4), "valid")
    
    def test_validity_3(self):
        self.assertEqual(checkValidity(5555555555554443, 3), "not valid")
                         
if __name__ == '__main__':
    unittest.main()
