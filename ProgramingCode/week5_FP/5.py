def ulti(a, b):
    return (a, b)


def dist(lst, n):
    return list([ulti(number, n) for number in lst])


print(dist([1, 2, 3], 4))
