def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(power(float(input("Введите действительное полож число, х = ")), int(input("Введите целое отр число, y = "))))
