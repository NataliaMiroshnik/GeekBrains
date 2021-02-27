class Data:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def convert(cls, data):
        day, month, year = map(int, data.split('-'))
        print(type(day), type(month), type(year))

    @staticmethod
    def valid(data):
        day, month, year = map(int, data.split('-'))
        if year > 2021 or month > 12 or day > 31 or (day > 30 and (month == 2 or month == 4 or month == 6 or month == 9 or month == 11)):
            print('Что-то в вашей дате не так...')
        else:
            print('Дата реальна')


b_day = '12-11-1987'
print(Data.convert(b_day))
print(Data.valid(b_day))