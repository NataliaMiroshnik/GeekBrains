class Stationery:
    def __init__(self, title='name'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')

stat = Stationery()
stat.draw()

mark = Handle()
pen = Pencil()

mark.draw()
pen.draw()