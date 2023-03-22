"""
Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).
В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод
"""
import time
from time import sleep


class TrafficLight:
    _color = 0
    _colors = ['красный', 'желтый ', 'зеленый']
    _times = [7, 2]

    def __init__(self, init_color=0, green_time=5):
        self._color = init_color
        self._times.append(green_time)

    def __str__(self):
        return self._colors[self._color]

    def _switch(self):
        print(self)
        time.sleep(self._times[self._color])
        self._color = self._color + 1 if self._color < 2 else 0

    def running(self):
        while True:
            self._switch()


traf_light = TrafficLight()
traf_light.running()
