my_f = open('test.txt', 'w', encoding='utf-8')
while True:
    line = input('Введите текст: ')
    if not line:
        break
    print(line, file=my_f)
    """используем функцию print для записи. Поскольку print добавляет пустую строку, можно не использовать \n"""

my_f.close()

my_f = open('test.txt', 'r', encoding='utf-8')
for line in my_f:
    print(line)
my_f.close()
