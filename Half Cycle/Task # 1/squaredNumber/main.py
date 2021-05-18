def squaredNumber():
    print("Please, insert a number")
    number = input()
    if number.isdigit() and int(number) >= 0:
        number = int(number)
        return number * number
    return "That was not a number!"


print(squaredNumber())
