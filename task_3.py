def type_logger(func):
    def wrapper(n):
        func(n)
        print(f"calc_cube{n, type(n)}")

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
