def takes_positive(func):
    def wrapper(*args, **kwargs):
        lst = [i for i in args] + [j for j in kwargs.values()]
        try:
            for i in lst:
                if type(i) != int:
                    raise TypeError
                elif i <= 0:
                    raise ValueError
        except TypeError as err:
            raise err
        except ValueError as err:
            raise err
        else:
            return func(*args, **kwargs)
    return wrapper
