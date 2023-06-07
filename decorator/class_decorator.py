class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"{self.func.__name__} was called with the following arguments")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        self.func(*args, **kwargs)
        print("Decorator is still operating")


@Decorator
def combiner(*args, **kwargs):
    print(f"Hello from the decorated function; received arguments: {args}, {kwargs}")


combiner("a", "b", k1="v1", k2="v2")
