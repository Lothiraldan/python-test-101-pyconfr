import unittest
from main import divisible_by_11


class DivisibleBy11TestCase(unittest.TestCase):

    def test_divisible_11(self):
        self.assertTrue(divisible_by_11(11))

    def test_not_divisible_9(self):
        self.assertTrue(divisible_by_11(9))

if __name__ == '__main__':
    unittest.main()
