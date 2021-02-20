class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name (self):
        return f"Полное имя сотрудника {self.name} {self.surname}"

    def get_total_income(self):
        return f"Доход с учетом премии составляет {sum(self._income.values())}"

manager = Position('Имя', 'Фамилия', 'должность', 72871, 23322)
print(manager.get_full_name())
print(manager.position)
print(manager.get_total_income())
