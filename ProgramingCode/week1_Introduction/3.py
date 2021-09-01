def gcd(a, b):
    while(b != 0):
        temp = a % b
        a = b
        b = temp
    return a


print(gcd(24, 36))
