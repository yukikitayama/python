class Tank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__level = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, amount):
        self.__level = amount

    @level.deleter
    def level(self):
        self.__level = None


t = Tank(10)
print(t.level)
t.level = 1
print(t.level)
del t.level
print(t.level)

