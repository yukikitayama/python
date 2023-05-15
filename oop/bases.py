class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


print(SuperOne.__bases__, SuperOne.__bases__[0].__name__)
print(SuperTwo.__bases__, SuperTwo.__bases__[0].__name__)
print(Sub.__bases__, Sub.__bases__[0].__name__)
