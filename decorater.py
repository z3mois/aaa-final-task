from functools import wraps


def log(params: str):
    """параметр - шаблон для вывода информации"""
    def outer_wrapper(func):
        @wraps(func)
        def inner_wrapper(pizza) -> str:
            """вовзращаем шаблон c названием функции,
            названием пиццы и временем исполнения"""
            res = func(pizza)
            return params.format(func.__name__, pizza.pizza, res)

        return inner_wrapper

    return outer_wrapper
