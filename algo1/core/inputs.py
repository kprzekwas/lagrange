from core.models import Data


def collection_size():
    while True:
        try:
            x = input("Podaj liczność zbioru (od 1 do 6): ")
            if 2 <= int(x) <= 6:
                return int(x)
            else:
                print("Podana liczebność powinnna być liczba całkowitą od 2 do 6")
        except Exception as e:
            print(e)


def data_table(collection_size: int):
    data_list = []
    for i in range(0, collection_size):
        y = int(input(f"Podaj rzędną wezła x{i}, która jest liczbą całkowitą przedziału [1;10] "))
        if y < 1 or y > 10:
            raise Exception(" y ma być z przedziału [1;10]")
        data_list.append(Data(y))

    return data_list


