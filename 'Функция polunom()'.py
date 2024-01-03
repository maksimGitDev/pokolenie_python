def polynom(x):
    n = x**2 + 1
    polynom.values = polynom.__dict__.setdefault('values', set()).add(n)
    return n
