import sys


def print_decorator(func):
    def wrapepr(*args, sep=' ', end=''):
        res = [i for i in args]
        res = sep.join(res) + end
        res = res.upper()
        return sys.stdout.write(res)
    return wrapepr


@print_decorator
def print(*args, sep=' ', end=''):
    return args
