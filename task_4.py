def val_checker(a):
    def my_deco(func):
        def wrapper(x):
            if not a(x):
                raise ValueError
            return func(x)

        return wrapper
    return my_deco


@val_checker(lambda x: x > 0)
def calc_cube(x):
    print(x ** 3)


calc_cube(5)
