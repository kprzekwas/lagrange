from core.lagrange import lagrange, lagrange_multipers, print_multipliers
from core.inputs import collection_size, data_table


"""Podstawowy moduł do uruchamiania apliakcji i zbierania informacji od użytkownika"""
if __name__ == "__main__":
    knots_size = collection_size()
    knots_list = data_table(knots_size)
    multipliers_list = lagrange_multipers(knots_list, knots_size)
    print_multipliers(multipliers_list)
    lagrange(multipliers_list, knots_list)





