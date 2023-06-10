class Car:
    def __init__(self, vin):
        print("__init__")
        self.vin = vin
        self.brand = ""

    @classmethod
    def including_brand(cls, vin, brand):
        print("classmethod")
        _car = cls(vin)
        _car.brand = brand
        return _car


c1 = Car("A")
print()
c2 = Car.including_brand("B", "Toyota")
print()

print(c1.vin, c1.brand)
print(c2.vin, c2.brand)
