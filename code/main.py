class Number(object):

    def __init__(self, number):
        self.number = number

    def divisible_by_11(self):
        """Uses above criterion to check if number is divisible by 11"""
        if self.number == 0:
            return False
        string_number = str(self.number)
        alternating_sum = sum([(-1) ** i * int(d) for i, d
                               in enumerate(string_number)])
        return alternating_sum == 0
