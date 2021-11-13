x = int(input("Введите целое число: "))
max = 0
while x > 0:
    if x % 10 > max:
        max = x % 10
    x = x // 10
print(max)
