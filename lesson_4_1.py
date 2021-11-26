from sys import argv


def zp():
    try:
        time, rate, bonus = map(float, argv[1:])
        if time or rate == 0:
            print("Отработанное время или зарплата не могут быть равны нулю")
        else:
            print(time * rate + bonus)
    except ValueError:
        print("Необходимо ввести только три цифры через пробел.")


zp()
