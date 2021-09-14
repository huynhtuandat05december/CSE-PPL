def square(n):
    return n*n


def lstSquare(size):
    result = []
    result = [square(number) for number in range(1, size+1)]
    return result


print(lstSquare(3))
