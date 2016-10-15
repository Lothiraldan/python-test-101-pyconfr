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

        self.assertEqual(result, False)

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


def test_floor_half():
    number = Number(2.5)

    assert number.floor() == 3


def test_floor_pi():
    number = Number(math.pi)

    assert number.floor() == 4

if __name__ == '__main__':
    unittest.main()
