"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
from timeit import Timer


def inp_set(prompt):
    set_x = set()
    n = int(input(f"Количество элементов {prompt} множества? "))
    for i in range(n):
        set_x.add(input(f"Введите элемент #{i + 1} {prompt} множества: "))
    return set_x


def main():
    set_n = inp_set("первого")
    set_m = inp_set("второго")
    set_nm = list(set_n & set_m)
    print(f"итоговое множество: {sorted(set_nm)}")


if __name__ == "__main__":

    t = Timer("main()", "from __main__ import main")
    print(t.timeit(number=1))
