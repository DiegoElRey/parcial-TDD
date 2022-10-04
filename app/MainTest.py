import unittest as test
import Main as api

class MainTest (test.TestCase):
    def setUp(self):
        self.main = api
    def test_ShouldReturnTrueIsPrimeNumber(self):
        self.main = api
        self.assertEqual(self.main.validate_number(5), True)
    def test_ShouldReturnFalseIsNotAPrimeNumber(self):
        self.main = api
        self.assertEqual(self.main.validate_number(1), False)
    def test_ShouldReturnFalseIsNotsPrimeNumber(self):
        self.main = api
        self.assertEqual(self.main.validate_number(0), False)
    def testShouldReturnFalseIsNotIsAPrimeNumber(self):
        self.main = api
        self.assertEqual(self.main.validate_number(4), False)
    
test.main()