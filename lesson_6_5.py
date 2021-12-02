class Stationary:
    def __init__(self, title="Предмет для записи"):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки ручкой')


class Pencil(Stationary):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки карандашом')


class Handle(Stationary):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки маркером')


stat = Stationary()
pen = Pen('ручку фирмы J')
pencil = Pencil('карандаш фирмы  F')
handle = Handle('маркер фирмы V')

predmet = [stat, pen, pencil, handle]

for i in predmet:
    i.draw()
