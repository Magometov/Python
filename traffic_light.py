import time


class TrafficLight:
    __color = 'Red'

    def running(self):
        while True:
            print(self.__color)
            time.sleep(7)
            self.__color = 'Yellow'
            print(self.__color)
            time.sleep(2)
            self.__color = 'Green'
            print(self.__color)
            time.sleep(7)
            self.__color = 'Red'


a = TrafficLight()
a.running()
