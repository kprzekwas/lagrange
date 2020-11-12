from fractions import Fraction

"""Klasy zawierające modele obiektów, które są wykorzystywane w projekcie"""


class Data:
    """ f(x) as y = 1/x """

    def __init__(self, y):
        self.x = Fraction(1, y)
        self.y = y

    def __str__(self):
        return "x = {0}, y = {1}".format(self.x, self.y)


class Frac:
    """Klasa definiująca mnożnik Lagrange'a"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0})/({1})".format(self.x, self.y)