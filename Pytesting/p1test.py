import unittest
from p1 import prime

class TestP1(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(12.9, prime.printprime(10))