class Person:
    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight


p1 = Person(30)
p2 = Person(35)

print(p1 + p2)

