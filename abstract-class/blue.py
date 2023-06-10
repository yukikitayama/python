import abc


class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass


class GreenField(BluePrint):
    # pass
    def hello(self):
        print("Welcome to Green Field")


gf = GreenField()
gf.hello()

# bp = BluePrint()


