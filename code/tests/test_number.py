import math
import unittest

import pytest

from main import Number


class IsOddTestCase(unittest.TestCase):

    def test_is_odd_1(self):
        number = Number(1)

        result = number.is_odd()

        self.assertTrue(result)

    def test_is_not_odd_4(self):
        number = Number(4)

        result = number.is_odd()

        self.assertFalse(result, "4 shouldn't be odd")

    # def test_first_ten_numbers(self):
    #     for i in range(10):
    #         number = Number(i * 1)

    #         result = number.is_odd()

    #         self.assertTrue(result)


@pytest.mark.parametrize("number", range(10))
def test_first_ten_numbers(number):
    number = Number(number * 2)

    result = number.is_odd()

    assert result is False


def test_ceil_int():
    number = Number(3)
    assert number.ceil() == 3

if __name__ == '__main__':
    unittest.main()
