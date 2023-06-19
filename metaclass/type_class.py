for t in (int, list, type):
    print(type(t))

for element in (1, "a", True):
    print(element, element.__class__, type(element))

print()

Dog = type("Dog", (), {})

print(Dog.__name__)
print(Dog.__class__)
print(Dog.__bases__)
print(Dog.__dict__)
print()


def bark(self):
    print("Woof")


class Animal:
    def feed(self):
        print("Feeding")


Dog = type("Dog", (Animal,), {"age": 0, "bark": bark})

print(Dog.__name__)
print(Dog.__class__)
print(Dog.__bases__)
print(Dog.__dict__)

doggy = Dog()
doggy.feed()
doggy.bark()
print(doggy.__dict__)
print()


