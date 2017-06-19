# coding=utf-8
import random

"""
10.3: Lottery
"""


def lottery(numbers):
    lowerBound = 1
    upperBound = 45
    number = 0
    lottery_numbers = []
    new_number = 0

    if numbers > 45:
        print "Maximum 45 numbers: set to 45"
        numbers = 45

    while number < numbers:
        new_number = random.randint(lowerBound, upperBound)
        if new_number not in lottery_numbers:
            lottery_numbers.append(new_number)
            number += 1

    return lottery_numbers


if __name__ == '__main__':
    print 70* "-"+"\nWelcome to the Lottery numbers generator."

    while True:
        try:
            number = int(raw_input("\nPlease enter how many random numbers would you like to have:\n"))
            lottery_num = lottery(number)
            print 70* "-"+"\nYour lottery numbers: {}\n".format(sorted(lottery_num)) + 70* "-"
            break
        except:
            print ("Enter a number")


