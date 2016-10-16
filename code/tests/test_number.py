import math
import unittest

import pytest
from hypothesis import given  # This is how we will define inputs
from hypothesis.strategies import integers  # This is the type of input we will use

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


def test_get_sign_1():
    assert Number(1).get_sign() == '+'


def test_get_sign_minus_1():
    assert Number(-1).get_sign() == '-'


def test_get_sign_zero():
    assert Number(0).get_sign() == '+'


@pytest.mark.parametrize("number", range(1, 10))
def test_is_divisible_by_11(number):
    assert Number(number * 11).divisible_by_11() == True

    assert Number(number * 11 + 1).divisible_by_11() == False


@given(number=integers(min_value=1))  # This is the main decorator
def test_divisible_by_11(number):
    assert Number(11 * number).divisible_by_11() == True

if __name__ == '__main__':
    unittest.main()
