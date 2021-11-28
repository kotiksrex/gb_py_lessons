lines = [line.strip() for line in open('test.txt', encoding='utf-8')]
for index, value in enumerate(lines, 1):
    number_of_words = len(value.split())
    print(f'Строка {index} содержит {number_of_words} слов')
