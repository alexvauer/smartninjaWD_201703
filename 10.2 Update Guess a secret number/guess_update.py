# coding=utf-8
import random
"""
Homework 10.2: Update the "Guess a secret number" game
"""


def main():
    lowerBound = 1
    upperBound = 20

    secret = random.randint(lowerBound, upperBound)
    print 45 * "*"
    print "Welcome to the \'Guess the secret number game\'\n" + 45 * "*"

    while True:

        try:
            number = raw_input("Make your Guess(1-20): ")

            if int(number) == secret:
                print 45 * "*", "\n\n", secret, "is right. Congratulation", "\n\n", + 45 * "*"

                break

            else:
                print "\n   ", number, "is wrong. Try again..\n"

        except:
            print "Please use whole numbers:"


if __name__ == '__main__':
    main()
