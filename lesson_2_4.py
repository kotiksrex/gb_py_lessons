my_str = input("введите слова, разделенные пробелом ").split()
for n, el in enumerate(my_str, 1):
    if len(el) <= 10:
        print(f"{n}) {el}")
    else:
        print(f"{n}) {el[:10]}")
        n += 1
