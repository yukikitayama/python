for t in (int, list, type):
    print(type(t))

for element in (1, "a", True):
    print(element, element.__class__, type(element))

Dog = type("Dog", (), {})

print(Dog.__name__)
print(Dog.__class__)
print(Dog.__bases__)
print(Dog.__dict__)

