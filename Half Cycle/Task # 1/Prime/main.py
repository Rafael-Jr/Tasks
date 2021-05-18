from math import sqrt


def is_prime():
    number = input()
    if not number.isdigit():
        return "That was not a number!"

    number = int(number)
    if number > 0 and all(number % i for i in range(1, int(sqrt(number)) + 1)):
        return 1
    return 0


print("Please, insert a number")
print(is_prime())
