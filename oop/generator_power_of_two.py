def powers_of_two(n):
    power = 1

    for _ in range(n):
        yield power
        power *= 2


for powered in powers_of_two(8):
    print(powered)


def fibonacci(n):
    p1 = 1
    p2 = 1

    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            fibed = p1 + p2
            p2 = p1
            p1 = fibed
            yield fibed


for fib in fibonacci(10):
    print(fib)