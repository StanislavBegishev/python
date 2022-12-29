# 2) Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения
# данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить
# метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.



class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


r = MassCount(25, 10000, 125)
print(r.mass())
