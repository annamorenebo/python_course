"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
word_list = ("разработка", "администрация", "protocol", "standart")
for word in word_list:
    word_bytes = word.encode('utf-8')
    print(f"bytes:{word_bytes}")
    word_dec = word_bytes.decode('utf-8')
    print(f"decode:{word_dec}")

