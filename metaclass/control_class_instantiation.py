def greet(self):
    print("Hello")


class My_Meta(type):
    def __new__(mcs, name, bases, dictionary):
        if "greet" not in dictionary:
            dictionary["greet"] = greet

        obj = super().__new__(mcs, name, bases, dictionary)

        return obj


class C1(metaclass=My_Meta):
    pass


class C2(metaclass=My_Meta):
    def greet(self):
        print("Hello world")


obj1 = C1()
obj1.greet()
obj2 = C2()
obj2.greet()



