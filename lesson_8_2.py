class Division(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_input(num, mum):
    try:
        num, mum = float(num), float(mum)
        if mum == 0:
            raise Division("На ноль делить нельзя!")
        return round(num / mum, 3)
    except ValueError:
        return "Value Error"
    except Division as err:
        return err
