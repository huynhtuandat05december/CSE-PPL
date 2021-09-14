def dist(lst, n):
    return list(map(lambda x: (x, n), lst))


print(dist([1, 2, 3], 4))
