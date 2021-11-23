def personal_info(**kwargs):
    """задаем функцию, которая может принимать неопределенное число именованных параметров"""
    return ' '.join(kwargs.values())


"""возвращаем значение функции. Используем метод join для объединения списка в строку и метод values.
    Метод values() возвращают список всех значений, доступных в данном словаре."""

print(personal_info(name=input("Enter your name: "), surname=input("Enter your surname: "),
                    birthday=input("Enter your birthday: "), city=input("Enter your city: "),
                    email=input("Enter your email: "),
                    phone_number=input("Enter your phone number: ")))
"""Вызываем заданную функцию напрямую в input"""
