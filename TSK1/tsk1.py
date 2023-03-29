"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
"""
import re
import csv

files = ["info_1.utf8.txt", "info_2.utf8.txt", "info_3.utf8.txt"]
prop_names = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
prop_re = re.compile(f"({'|'.join(prop_names)}):\\s+(.+)")


def get_data(file_list):
    res = []
    for file_name in file_list:
        props = {}
        with open(file_name, 'r') as fl:
            for line in fl.readlines():
                m = prop_re.match(line)
                if m is not None:
                    props[m[1]] = m[2]

        res.append(props)

    return res


def write_to_csv(csvfile):
    csvfile.writerow(prop_names)
    for item in get_data(files):
        csvfile.writerow([item.get(col) for col in prop_names])


with open('result.csv', 'w', newline='') as f:
    write_to_csv(csv.writer(f))
