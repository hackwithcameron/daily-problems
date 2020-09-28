def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    """
    Passes the 'cons' function as an argument allowing for the 'first' function to
    be passes as variable f.
    :param pair: cons function object
    :return: First number in pair
    """
    def first(x, y):
        return x
    return pair(first)


def cdr(pair):
    """
    Passes the 'cons' function as an argument allowing for the 'last' function to
    be passes as variable f.
    :param pair: cons function object
    :return: Last number in pair
    """
    def last(x, y):
        return y
    return pair(last)


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))


