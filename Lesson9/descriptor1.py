class Numeric:
    def __set__(self, instance, value):
        if type(value) == int or type(value) == float:
            instance.__dict__[self.my_attr] = value
        else:
            raise TypeError("Значение должно быть числом")

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    _length = Numeric()
    _width = Numeric()

    mass_metr = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_cover(self):
        return self._length * self._width * self.thickness * self.mass_metr


road = Road(5000, "kjhg")
print(f"Масса дорожного покрытия: {road.road_cover() / 1000} тонн")
