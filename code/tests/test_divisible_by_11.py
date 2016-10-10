import unittest
from main import divisible_by_11


class DivisibleBy11TestCase(unittest.TestCase):

    def test_with_11(self):
        self.assertTrue(divisible_by_11(11), True)

if __name__ == '__main__':
    unittest.main()
