def calc():
    try:
        arg_1 = float(input("Укажите первое число: "))
        arg_2 = float(input("Укажите второе число: "))
        s_full = arg_1 / arg_2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider"

    return round(s_full, 2)


print(calc())
