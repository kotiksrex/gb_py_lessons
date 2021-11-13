print("It's lesson_1 task 2")
a = int(input(' Введите время в секундах: '))
h = a // 36000
hh = a % 36000 // 3600
m = a % 3600 // 600
mm = a % 3600 % 600 // 60
s = a % 60 // 10
ss = a % 60 % 10
print(f"{h}{hh}:{m}{mm}:{s}{ss}")
