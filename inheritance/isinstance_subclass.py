class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


land_vehicle = LandVehicle()

print(isinstance(land_vehicle, Vehicle))
