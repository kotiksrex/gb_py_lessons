class Store:
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'год выпуска': self.year}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.year}'

    def reception(self):
        # print(f'Для выхода - Q, продолжение - Enter')
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_y = int(input(f'Введите год выпуска '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'год выпуска': unit_y}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Store.reception(self)


class Printer(Store):
    def __init__(self, name, price, year, paper_size):
        self.paper_size = paper_size
        super().__init__(name, price, year)


class Scanner(Store):
    def __init__(self, name, price, year, dpi_color):
        self.dpi_color = dpi_color
        super().__init__(name, price, year)


class Copier(Store):
    def __init__(self, name, price, year, paper_speed):
        self.paper_speed = paper_speed
        super().__init__(name, price, year)


class Storehouse(Store):
    __stock = dict()
    __consumption = dict()


unit_1 = Printer('hp', 2000, 5, 2000)
unit_2 = Scanner('Canon', 1200, 5, 2001)
unit_3 = Copier('Xerox', 1500, 1, 2020)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())



