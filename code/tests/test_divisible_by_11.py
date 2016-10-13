import unittest
from main import Number


class DivisibleBy11TestCase(unittest.TestCase):

    def test_divisible_11(self):
        number = Number(11)

        result = number.divisible_by_11()

        self.assertTrue(result)

    def test_not_divisible_9(self):
        number = Number(9)

        result = number.divisible_by_11()

        self.assertTrue(result, "9 should be divisible by 11")

if __name__ == '__main__':
    unittest.main()
