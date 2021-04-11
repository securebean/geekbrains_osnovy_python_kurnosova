
def type_logger(func):
    def logger(*args):
        list_args = []
        for arg in args:
            list_args.append(f'{str(arg)}: {type(arg)}')
        print(', '.join(list_args))    # выводит данные о каждом аргументе через запятую
        print(type(func(*args)))    # выводит тип значения функции
    return logger


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc(x, y):
    return x * y


calc_cube(5)
calc(7, 8)
