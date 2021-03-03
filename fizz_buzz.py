def fizz_buzz():
    result = [None] * 100
    for number in range(1, 100, 1):
        if number % 3 == 0:
            result[number - 1] = "Fizz"

    print(result)
    return result
