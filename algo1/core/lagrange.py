import sympy

from core.models import Frac

"""Główny moduł zawierające funkcje obliczania wielomianu na podstawie węzłów podnaych przez użytkownika"""


def lagrange_multipers(lista, elemets_number: int):
    """główna funkcja obliczająca mnożniki Lagrangea"""
    x = sympy.var('x')
    multiplier_list = []
    for i in range(elemets_number):
        list_l = []
        for k in range(elemets_number):
            if k != i:
                """Obliczanie każdego składnika mnożnika"""
                fraction = Frac(x - lista[k].x, lista[i].x - lista[k].x)
                list_l.append(fraction)
        multiplier_numerator = 1
        multiplier_denominator = 1
        """Składanie wszystkich mnożników"""
        for mnoznik in list_l:
            multiplier_numerator = multiplier_numerator * mnoznik.x
            multiplier_denominator = multiplier_denominator * mnoznik.y
        multiplier = Frac(multiplier_numerator, multiplier_denominator)
        multiplier_list.append(multiplier)
    return multiplier_list


def lagrange(multipliers_list, knots_list):
    """Składanie wszystkich mnożników z wartościami"""
    print("Wielomian interpolujacy ma postać: ", end='')
    for i in range(len(multipliers_list)):
        print(f"{knots_list[i].y}*[{multipliers_list[i]}]", end='')
        if i < len(multipliers_list)-1:
            print(" + ", end='')
        else:
            print("\n")


def print_multipliers(multipliers_list: list):
    """Wypisywanie mnożników"""
    for i in range(len(multipliers_list)):
        print(f"Mnożnik wynosi l({i}): {multipliers_list[i]}")