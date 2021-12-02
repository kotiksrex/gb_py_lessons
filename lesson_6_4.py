class Car:
    # atributes
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'текущая скорость {self.name} сотавляет {self.speed} км/час'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        # super поддтяивает методы выше по дереву наследования
        super().__init__(speed, color, name, is_police=False)

    # переопределение базового метода родителя у потомка
    def show_speed(self):
        print(f'Текущая скорость городской машинки {self.name} составляет {self.speed} км/час')

        if self.speed > 40:
            return f'Скорость {self.name} превышает допустимую для городского авто'
        else:
            return f'Скорость {self.name} находится в пределах нормы'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    # переопределение базового метода родителя у потомка
    def show_speed(self):
        print(f'Текущая скорость рабочей машинки {self.name} составляет {self.speed} км/час')

        if self.speed > 60:
            return f'Текущая скорость {self.name} превышает допустимую для рабочей машинки'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)

    def police(self):
        if self.is_police:
            return f'{self.name} это полиция'
        else:
            return f'{self.name} это не полиция'


audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(30, 'White', 'Oka', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(lada.turn_left())
print(f'Сначала {oka.turn_right()}, потом {audi.stop()}')
print(f'{lada.go()} {lada.show_speed()}')
print(f'{lada.name}  {lada.color}')
print(f' {audi.name} - это полиция? {audi.is_police}')
print(f' {lada.name}  - это полиция? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())
