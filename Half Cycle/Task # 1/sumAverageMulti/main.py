import statistics as stats
from functools import reduce


def sumAverageMulti():
    array = []
    for i in range(5):
        print("enter a number greater than or equal to 0")
        number = input()
        while not (number.isdigit()) or int(number) < 0:
            print("Correct the number, you insert: %s" % number)
            number = input()

        array.append(int(number))

    return "\nSum: " + str(sum(array)) \
           + "\nAverage: " + str(stats.mean(array)) \
           + "\nMultiplication: " + str(reduce(lambda x, y: x * y, array))


print(sumAverageMulti())
