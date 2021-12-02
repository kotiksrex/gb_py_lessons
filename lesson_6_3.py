class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return sum(self._income.values())


rab = Position("Василий", "Васильев", "Рыбак", 50000, 25000)
print(f" Имя и фамилия: {rab.get_full_name()}")
print(f" Кем работает: {rab.position}")
print(f" Сколько зарабатывает: {rab.get_total_income()} рублей")
