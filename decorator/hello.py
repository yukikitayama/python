def simple_hello():
    print("Hello from simple function!")


def simple_decorator(function):
    print(f"We are about to call {function.__name__}")
    return function


decorated = simple_decorator(simple_hello)
decorated()


@simple_decorator
def simple_hello2():
    print("Hello 2")


simple_hello2()

print()


def decorator_args(func):

    def internal(*args, **kwargs):
        print(f"Call: {func.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        func(*args, **kwargs)
        print(f"Decorator is operating")

    return internal


@decorator_args
def combiner(*args, **kwargs):
    print(f"Hello from decorated function with {args}, {kwargs}")


combiner("a", "b", a1="yes")
