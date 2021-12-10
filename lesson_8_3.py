class OnlyNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    try:
        value = input('Введите число в список или stop, если список завершен:')
        if value == 'q' or value == "stop":
            print(my_list)
            break
        if not value.isdigit():
            raise OnlyNumber("Только целые числа!")
        my_list.append(int(value))
    except OnlyNumber as ex:
        print(ex)
        continue
