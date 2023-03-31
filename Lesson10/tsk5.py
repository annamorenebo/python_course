"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!
"""
import chardet

import subprocess
import chardet

args = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for arg in args:

    ping_res = subprocess.Popen(arg, stdout=subprocess.PIPE)
    i = 0
    for line in ping_res.stdout:
        if i <= 11:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'))
            i += 1
        else:
            break


