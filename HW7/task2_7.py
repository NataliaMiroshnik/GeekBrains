class Clothes:
    def __init__(self, name):
        self.name = name

    def cost(self):
        pass


class Coat(Clothes):
    def __init__(self,name, size):
        Clothes.__init__(self, name)
        self.size = size

    @property
    def cost(self):
        return f"{round(self.size / 6.5 + 0.5, 1)}"


class Costumes(Clothes):
    def __init__(self,name, height):
        Clothes.__init__(self, name)
        self.height = height

    @property
    def cost(self):
        return f"{round(2 * self.height + 0.3, 1)}"

cloak = Coat('плащ', 76)
jacket = Costumes('пиджак', 176)
print(cloak.cost)
print(jacket.cost)
print(f"Расход ткани {cloak.cost + jacket.cost}")