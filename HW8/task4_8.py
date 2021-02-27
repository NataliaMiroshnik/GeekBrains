class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Pantry:
    """"Склад оргтехники"""
    pass


class OfficeEquipment:
    """"Оргтехника"""
    things = {}

    def __init__(self, name, series):
        self.name = name
        self.series = series

    @classmethod
    def reception(cls, thing):
        key, value = thing.split('-')
        if not value.isdigit():
            raise MyError('Внимание, количество товара должно быть число')
        cls.things[key]=value


class Printer(OfficeEquipment):
    """"Принтер"""
    def __init__(self, name, series, pr_number):
        OfficeEquipment.__init__(self, name, series)
        self.pr_number = pr_number


class Scanner(OfficeEquipment):
    """Сканер"""
    def __init__(self, name, series, color):
        OfficeEquipment.__init__(self, name, series)
        self.color = color


class Copier(OfficeEquipment):
     """Ксерокс"""
    def __init__(self, name, series, model):
        OfficeEquipment.__init__(self, name, series)
        self.model = model
