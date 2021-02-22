class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'налево':
            print('Машина повернула налево')
        elif direction == 'направо':
            print('Машина повернула направо')
        else:
            print('Машина не может повернуть в неизвестном направлении')

    def show_speed(self, speed):
        self.speed = speed

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Слишком быстро. Сбавьте до 60 км/ч')
        else:
            print('Ваша скорость = ', self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Слишком быстро. Сбавьте до 40 км/ч')
        else:
            print('Ваша скорость = ', self.speed)

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)
