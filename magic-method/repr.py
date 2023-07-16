class ProductionLine:
    def __init__(self, capacity):
        self.capacity = capacity

    def __repr__(self):
        return f"ProductionLine(capacity={self.capacity})"

    def __add__(self, other):
        return ProductionLine(self.capacity + other.capacity - 50)


prod1 = ProductionLine(100)
prod2 = ProductionLine(200)

print(prod1 + prod2)
