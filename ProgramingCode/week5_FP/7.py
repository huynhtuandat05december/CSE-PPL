

def increase(a):
    return a+1


def square(a):
    return a*a


def double(a):
    return a+a


def compose(*functions):
    if len(functions) < 2:
        raise TypeError

    def inner(arg):
        for f in reversed(functions):
            arg = f(arg)
        return arg
    return inner


f = compose(increase, square, double)
print(f(3))
