"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

str_list = ['attribute', 'класс', 'функция', 'type']

for s in str_list:
    try:
        my_string = str(bytes(s, encoding='utf-8'))[2:-1]
        if not my_string.isalpha():
            raise ValueError(f"слово ", {s}, " нельзя представить в байтовом формате")

    except ValueError as err:
        print(err)








