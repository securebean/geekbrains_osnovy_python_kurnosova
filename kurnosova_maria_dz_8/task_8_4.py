
def val_checker(exp):
    def _checker(func):
        def checker(x):
            if exp(x):
                return func(x)
            else:
                raise ValueError(f'wrong val {x}')
        return checker
    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
