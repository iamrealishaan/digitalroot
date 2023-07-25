def digitalroot(number):
    while number >= 10:
        total = 0
        while number > 0:
            total += number % 10
            number //= 10
        number = total
    return number

num = int(input("enter Your number:", ))
result = digitalroot(num)
print(result)
