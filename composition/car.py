class Car:
    def __init__(self, engine):
        self.engine = engine


class GasEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print(f"Starting {self.hp}hp gas engine")


class DieselEngine:
    def __init__(self, horse_power):
        self.hp = horse_power

    def start(self):
        print(f"Starting {self.hp}hp diesel engine")


my_car = Car(GasEngine(4))
my_car.engine.start()
a_car = Car(DieselEngine(6))
a_car.engine.start()



