from math import pi
def my_sum(*args):
    return sum(args)

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return pi * self.r * self.r
