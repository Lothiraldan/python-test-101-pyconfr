#HSLIDE

## Pycon-fr 2016

Python monkey-patching in production.

#VSLIDE

## About-me @lothiraldan

 * Python developer

<img src="images/me.png" width="400" height="400"/>

#VSLIDE

## Sqreen.io

I work at sqreen.io where we bring security to every developer.

<img src="images/sqreen.png" width="400" height="400"/>

#HSLIDE

## Source code is available online

https://github.com/Lothiraldan/python-test-101-pyconfr

#HSLIDE

## What is a test?

>Checking that one aspect of the application behaves like expected. <!-- .element: class="fragment" -->

#HSLIDE

## Testing, why?

<img src="images/tester-douter.jpg.jpg" height="400"/> <!-- .element: class="fragment" -->

#VSLIDE

## Seriously

* Ensure code quality. <!-- .element: class="fragment" -->
* Check that there is no regression. <!-- .element: class="fragment" -->
* Detect new bugs. <!-- .element: class="fragment" -->

#VSLIDE

## Real-reason

>"Did I just break something else with that change?" With automated tests, when I start to feel stress, I run the tests. Tests are the Programmer’s Stone, transmuting fear into boredom. "No, I didn’t break anything. The tests are all still green." - Kent Beck


#HSLIDE

## System Under Test

Let's take a function that test divisibility by 11 that use the following property:

>A number is divisible by 11 if and only if the alternating (in sign) sum of the number’s digits is 0.

#VSLIDE

## Code

Let's write the function (file `main.py`):

```python
class Number(object):

    def __init__(self, number):
        self.number = number

    def divisible_by_11(self):
        """Uses above criterion to check if number is divisible by 11"""
        string_number = str(self.number)
        alternating_sum = sum([(-1) ** i * int(d) for i, d
                               in enumerate(string_number)])
        return alternating_sum == 0
```

#HSLIDE

## Unittest

Unittest is a standard module in the Python standard library, it helps us structure our tests and set a standard for test discovery and running.

#VSLIDE

## Unittest 101

```python
import unittest

class DivisibleBy11TestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_divisible_by_11(self):
        pass

if __name__ == '__main__':
    unittest.main()
```

#VSLIDE

## Line by line

Import the standard module:

```python
import unittest
```

#VSLIDE

## Line by line

Create a TestCase, a class which usually test the same SUT. Each test will share the setUp and tearDown methods.

```python
class DivisibleBy11TestCase(unittest.TestCase):
```

#VSLIDE

## Line by line

The `setUp` method can be used for initializing an environment for all the test methods of the TestCase. It is called before each test method:

```python
    def setUp(self):
        self.connection = create_db_connection()

        self.sut = MyObject(self.connection)
```

In our case we don't need it. <!-- .element: class="fragment" -->

#VSLIDE

## Line by line

The `tearDown` method can be used to clean an environment after a test. It's called after each test method, even if they fails:

```python
    def tearDown(self):
        self.connection.close()
```

#VSLIDE

## Line by line

Our test code will go in methods that starts with `test_`.

```python
    def test_divisible_by_11(self):
        ...
```

#VSLIDE

## Line by line

These following lines helps us launch directly the tests when executing the file (with `python test.py`):

```python
if __name__ == '__main__':
    unittest.main()
```

#VSLIDE

## First test

Let's start with a simple example (file `tests/test_divisible_by_11.py`):

```python
import unittest
from main import divisible_by_11

class DivisibleBy11TestCase(unittest.TestCase):

    def test_divisible_11(self):
        number = Number(11)

        result = number.divisible_by_11()

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```

#VSLIDE

## Launch it

Let's launch it:

```bash
$> python -m tests.test_divisible_by_11
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

#VSLIDE

## Verbose mode

Out first test is passing, let's try again with more details:

```bash
$> python -m tests.test_divisible_by_11
test_with_11 (__main__.DivisibleBy11TestCase) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

#VSLIDE

## Let's add a second one

```python
class DivisibleBy11TestCase(unittest.TestCase):

    def test_not_divisible_9(self):
        number = Number(9)

        result = number.divisible_by_11()

        self.assertTrue(result)
```

#VSLIDE

## Launch it

```bash
$> python -m tests.test_divisible_by_11
test_divisible_11 (__main__.DivisibleBy11TestCase) ... ok
test_not_divisible_9 (__main__.DivisibleBy11TestCase) ... FAIL

======================================================================
FAIL: test_not_divisible_9 (__main__.DivisibleBy11TestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ".../tests/test_divisible_by_11.py", line 11, in test_not_divisible_9
    self.assertTrue(divisible_by_11(9))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 2 tests in 0.000s

FAILED (failures=1)
```

#HSLIDE

## Launch it with a better test runner

```bash
pip install pytest pytest-sugar
```

```bash
pytest tests -v
```

#VSLIDE?image=images/pytest.png

#HSLIDE

## Anatomy of a test

```python
    def test_something(self):
        preparation()

        execution()

        assertions()
```

#VSLIDE

## Preparation

In the preparation phase, we prepare everything for being able to execute our test scenario. 

#VSLIDE

## Execution

In the execution phase, we call some functions and methods that should either return something or alter something in the environment.

#VSLIDE

## Assertions

In the assertions phase, we check that returns is what we expect or the environment has been altered the way we expect it to be.

#VSLIDE

## List of assertions

* assertEqual
* assertNotEqual
* assertTrue
* assertFalse
* ...

https://docs.python.org/3/library/unittest.html?highlight=unittest#assert-methods

#VSLIDE

## List of assertions

Each of these methods returns meaningfull error messages to help you quickly debug your tests. But we can customize them.

#VSLIDE

## Message customization

```python
class DivisibleBy11TestCase(unittest.TestCase):

    def test_not_divisible_9(self):
        number = Number(9)

        result = number.divisible_by_11()

        self.assertTrue(result, "9 should be divisible by 11")
```

#VSLIDE

## Launch it again

```python
tests/test_divisible_by_11.py::DivisibleBy11TestCase::test_divisible_11 PASSED
tests/test_divisible_by_11.py::DivisibleBy11TestCase::test_not_divisible_9 FAILED

======================================== FAILURES ========================================
_______________________ DivisibleBy11TestCase.test_not_divisible_9 _______________________

self = <tests.test_divisible_by_11.DivisibleBy11TestCase testMethod=test_not_divisible_9>

    def test_not_divisible_9(self):
        number = Number(9)

        result = number.divisible_by_11()

>       self.assertTrue(result, "9 should be divisible by 11")
E       AssertionError: 9 should be divisible by 11

tests/test_divisible_by_11.py:19: AssertionError
```

#VSLIDE

## Let's fix the `test_not_divisible_9` test using `assertEqual` or `assertNotEqual`.

#HSLIDE

## Test severals numbers

```python
    def test_first_eleven_multiples(self):
        for i in range(10):
            number = Number(11 * i)

            result = number.divisible_by_11()

            self.assertTrue(result)
```

#VSLIDE

## Should 0 be divisible by 11?

Let's not ask our mathematician friend and say no for the sake of the exercice.

The test is passing but it's not what we want.

#VSLIDE

## First rule of tests

>Tests can only prove the presence of features, not the absence of bugs.

#VSLIDE

## Fix the code

```python
    def divisible_by_11(self):
        """Uses above criterion to check if number is divisible by 11"""
        if self.number == 0:
            return False
        string_number = str(self.number)
        alternating_sum = sum([(-1) ** i * int(d) for i, d
                               in enumerate(string_number)])
        return alternating_sum == 0
```

#VSLIDE

## Rerun the tests

```python
tests/test_divisible_by_11.py::DivisibleBy11TestCase::test_divisible_11 PASSED
tests/test_divisible_by_11.py::DivisibleBy11TestCase::test_first_eleven_multiples FAILED
tests/test_divisible_by_11.py::DivisibleBy11TestCase::test_not_divisible_9 PASSED

======================================== FAILURES ========================================
___________________ DivisibleBy11TestCase.test_first_eleven_multiples ____________________

self = <tests.test_divisible_by_11.DivisibleBy11TestCase testMethod=test_first_eleven_multiples>

    def test_first_eleven_multiples(self):
        for i in range(10):
            number = Number(11 * i)

            result = number.divisible_by_11()

>           self.assertTrue(result)
E           AssertionError: False is not true

tests/test_divisible_by_11.py:27: AssertionError
================= 1 failed, 2 passed, 1 pytest-warnings in 0.02 seconds ==================
```

#VSLIDE

## Second rule of tests

>Don't use loops in tests! NEVER!

#VSLIDE

## Instead leverage your test framework

Using `pytest.mark.parametrize`

```python
import pytest

@pytest.mark.parametrize("number", range(10))
def test_first_eleven_multiples(self, number):
    number = Number(number * 11)

    result = number.divisible_by_11()

    assert result is True
```

#VSLIDE

## Output

```
tests/test_divisible_by_11.py::DivisibleBy11TestCase::test_divisible_11 PASSED
tests/test_divisible_by_11.py::DivisibleBy11TestCase::test_not_divisible_9 PASSED
tests/test_divisible_by_11.py::test_first_eleven_multiples[0] FAILED
tests/test_divisible_by_11.py::test_first_eleven_multiples[1] PASSED
tests/test_divisible_by_11.py::test_first_eleven_multiples[2] PASSED
tests/test_divisible_by_11.py::test_first_eleven_multiples[3] PASSED
tests/test_divisible_by_11.py::test_first_eleven_multiples[4] PASSED
tests/test_divisible_by_11.py::test_first_eleven_multiples[5] PASSED
tests/test_divisible_by_11.py::test_first_eleven_multiples[6] PASSED
tests/test_divisible_by_11.py::test_first_eleven_multiples[7] PASSED
tests/test_divisible_by_11.py::test_first_eleven_multiples[8] PASSED
tests/test_divisible_by_11.py::test_first_eleven_multiples[9] PASSED
```

#VSLIDE

```
======================================== FAILURES ========================================
_____________________________ test_first_eleven_multiples[0] _____________________________

number = <main.Number object at 0x1036b4590>

    @pytest.mark.parametrize("number", range(10))
    def test_first_eleven_multiples(number):
        number = Number(number * 11)

        result = number.divisible_by_11()

>       assert result is True
E       assert False is True

tests/test_divisible_by_11.py:31: AssertionError
================= 1 failed, 11 passed, 1 pytest-warnings in 0.04 seconds =================
```

#HSLIDE

## Doctests

#HSLIDE

## TDD

#HSLIDE

## Fuzzing

#HSLIDE

## Mutation testing

#HSLIDE
