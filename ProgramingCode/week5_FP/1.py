
def lstSquare(size):
    if (size > 0):
        return lstSquare(size-1)+[size*size]
    else:
        return []


print(lstSquare(3))
