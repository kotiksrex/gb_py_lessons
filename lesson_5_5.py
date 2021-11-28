from random import randint

with open('task_5_file.txt', 'w+', encoding='utf-8') as s_file:
    s_file.write(" ".join([str(randint(1, 100)) for _ in range(1000)]))
    s_file.seek(0)
    print(f"Сумма всех чисел - {sum(map(int, s_file.readline().split()))}")
