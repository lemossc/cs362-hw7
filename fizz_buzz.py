def fizz_buzz():
    result = []
    for number in range(1, 100, 1):
        if number % 3 == 0:
            result[number - 1] = "Fizz"

    print(result)
    return result
