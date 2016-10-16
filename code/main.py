class Number(object):

    def __init__(self, number):
        self.number = number

    def is_odd(self):
        """ Return True is the number is odd
        """
        return self.number % 2 == 1

    def ceil(self):
        """ Returns the largest integer value less than or equal to
        current number.
        >>> Number(2.5).ceil()
        3
        >>> import math
        >>> Number(math.pi).ceil()
        4
        """
        if self.number % 1 > 0:
            return int(self.number) + 1
        return self.number
