def check(numbers, target):
    result=True
    for number in numbers:
        if number <= target:
            return False
    return result

print(check([21,12,5,8],3))