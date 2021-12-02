class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, weight=25, thickness=5):
        return self._length * self._width * weight * thickness / 1000


road_1 = Road(5000, 20)
print(f' Вам понадобится {road_1.mass()} тонн асфальта')
