def big_container_decorator(deco_arg):

    def wrapper(func):
        def internal_wrapper(*args):
            func(*args)
            print(f"The whole order would be packed with {deco_arg}")
        return internal_wrapper

    return wrapper


def warehouse_decorator(deco_arg):

    def wrapper(func):
        def internal_wrapper(*args):
            func(*args)
            print(f"Wrapping items from {func.__name__} with {deco_arg}")
        return internal_wrapper

    return wrapper


@big_container_decorator("plain cardboard")
@warehouse_decorator("bubble foil")
def pack_books(*args):
    print(f"We'll pack books: {args}")


pack_books("Alice in Wonderland", "Winnie the Pooh")
