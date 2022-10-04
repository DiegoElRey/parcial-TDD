import unittest as test
import Main as api

class MainTest (test.TestCase):
    def setUp(self):
        self.main = api
    def testShouldReturnTrueIsPrimeNumber(self):
        self.main = api
        assert self.main.validate_number(5), True
    def testShouldReturnFalseIsNotAPrimeNumber(self):
        self.main = api
        assert self.main.validate_number(1), False
    def testShouldReturnFalseIsNotsPrimeNumber(self):
        self.main = api
        assert self.main.validate_number(0), False
    def testShouldReturnFalseIsNotIsAPrimeNumber(self):
        self.main = api
        assert self.main.validate_number(4), False
    
test.main()