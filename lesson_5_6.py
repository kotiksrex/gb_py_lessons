dic = {}
numbers = "1234567890 "

with open("text_6.txt", "r", encoding="utf-8") as d_file:
    for lin in d_file:
        science, hours = lin.split(":")
        dic[science] = sum(map(int, "".join([num for num in hours if num in numbers]).split()))
        print(dic)
