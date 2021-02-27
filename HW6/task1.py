from time import sleep

class TrafficLight:
    color = 'Цвет'

    def running(self):
        while True:
            print('Красный')
            sleep(7)
            print('Желтый')
            sleep(2)
            print('Зеленый')
            sleep(10)
            print('Желтый')
            sleep(2)


turn = TrafficLight()
turn.running()