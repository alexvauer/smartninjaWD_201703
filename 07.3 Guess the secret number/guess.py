# coding=utf-8
"""
Homework 7.3: Guess the secret number
"""

secret_number = 7

if __name__ == '__main__':

    print 45*"*"
    print "Welcome to the \'Guess the secret number game\'\n"+45*"*"


    while True:

        try:
            number = raw_input("Make your Guess(1-10): ")

            if int(number) == secret_number:
                print 45 * "*", "\n\n", secret_number, "is right. Congratulation", "\n\n", + 45 * "*"

                break

            else:
                print "\n", number, "is wrong. Try again..\n"

        except:
            print "Please use whole numbers:"