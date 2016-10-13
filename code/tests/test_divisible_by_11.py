import unittest

import pytest

from main import Number


class DivisibleBy11TestCase(unittest.TestCase):

    def test_divisible_11(self):
        number = Number(11)

        result = number.divisible_by_11()

        self.assertTrue(result)

    def test_not_divisible_9(self):
        number = Number(9)

        result = number.divisible_by_11()

        self.assertEqual(result, False, "9 should not be divisible by 11")

    @pytest.mark.parametrize("number", range(10))
    def test_first_eleven_multiples(self, number):
        number = Number(number)

        result = number.divisible_by_11()

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
