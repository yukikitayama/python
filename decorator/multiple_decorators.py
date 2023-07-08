def deco_outer(func):
    def wrapper():
        print("Outer decorator started")
        func()
        print("Outer decorator ended")
    return wrapper


def deco_inner(func):
    def wrapper():
        print("Inner decorator started")
        func()
        print("Inner decorator ended")
    return wrapper


@deco_outer
@deco_inner
def func():
    print("Called a function")


func()
