def product(numbers):
    result=1
    for number in numbers:
        result*=number
    return result

print(product([3,4,7,11]))
