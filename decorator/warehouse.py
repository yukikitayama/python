def warehouse_decorator(material):

    def wrapper(our_function):
        def internal_wrapper(*args):
            print(f"Wrapping items from {our_function.__name__} with {material}")
            our_function(*args)
            print()

        return internal_wrapper

    return wrapper


@warehouse_decorator("kraft")
def pack_books(*args):
    print("We'll pack books:", args)


pack_books("Alice in Wonderland", "Winnie the Pooh")

