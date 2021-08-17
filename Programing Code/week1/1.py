import math


def area(r):
    return r*r*math.pi


res = area(1.1)
expect = 3.8013271108436504
delta = 0.000000001
print((res > expect - delta) and (res < expect + delta))
