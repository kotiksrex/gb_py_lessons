from time import sleep


class TrafficLight:
    __color = "Черный"


def running():
    while True:
        print("\033[31m {}".format("Красный"))
        sleep(7)
        print("\033[33m {}".format("Желтый"))
        sleep(2)
        print("\033[32m {}".format("Зеленый"))
        sleep(7)
        print("\033[33m {}".format("Желтый"))
        sleep(2)


trafficlight = TrafficLight()
running()
