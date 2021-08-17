def sum_of_cube(target):
    result = 0
    for number in range(target):
        result += pow(number, 3)
    return result


print(sum_of_cube(8))
