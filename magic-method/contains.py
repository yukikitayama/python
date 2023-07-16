class Container:
    def __init__(self):
        self.buffer = []

    def add(self, item):
        self.buffer.append(item)

    def __contains__(self, item):
        return item in self.buffer


container = Container()
container.add(1)
container.add(2)
container.add(3)

print(1 in container)
print(4 in container)
