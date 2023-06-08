class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter += 1

    @classmethod
    def get_internal(cls):
        return f"# of objects created: {cls.__internal_counter}"


print(Example.get_internal())

e1 = Example(10)
print(Example.get_internal())

e2 = Example(99)
print(Example.get_internal())
print(e2.get_internal())
