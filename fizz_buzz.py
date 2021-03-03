def fizz_buzz():
    result = [None] * 100
    for number in range(1, 100 + 1, 1):
        if number % 3 == 0 and number % 5 == 0:
            result[number - 1] = "FizzBuzz"
        elif number % 3 == 0:
            result[number - 1] = "Fizz"
        elif number % 5 == 0:
            result[number - 1] = "Buzz"

    print(result)
    return result
