import unittest as test
from Main import validate_number, validate_fibonacci

class MainTest (test.TestCase):
   
    def testShouldReturnTrueIsPrimeNumber(self):
        self.assertEqual(validate_number(5), True)

    def testShouldReturnFalseIsNotAPrimeNumber(self):
        self.assertEqual(validate_number(1), False)

    def testShouldReturnFalseIsNotsPrimeNumber(self):
        self.assertEqual(validate_number(0), False)

    def testShouldReturnFalseIsNotIsAPrimeNumber(self):
        self.assertEqual(validate_number(4), False)

test.main()