def dist(lst, n):
    if len(lst):
        return [(lst[0], n)]+dist(lst[1:], n)
    else:
        return []


print(dist([1, 2, 3], 4))
