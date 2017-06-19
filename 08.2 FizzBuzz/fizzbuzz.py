# coding=utf-8
"""
fizzbuzz.py

User enters a number between 1 and 100
FizzBuzz program starts to count to that number (it prints them in the Terminal). In case the number is divisible with 3,
it prints "fizz" instead of the number. If the number is divisible with 5, it prints "buzz". If it's divisible with both
3 and 5, it prints "fizzbuzz".
"""

if __name__ == '__main__':

    while True:

        counter = 0

        try:
            number = int(raw_input("\nPlease enter the number to FizzBuzz to: "))

            if number < 1:
                print "\n[!] Please use positive numbers greater than 0\n"

            else:
                while counter < number:
                    counter += 1

                    if counter % 3 == 0 and counter % 5 != 0:
                        print "fizz"
                    elif counter % 5 == 0 and counter % 3 != 0:
                        print "buzz"
                    elif counter % 5 == 0 and counter % 3 == 0:
                        print "fizzbuzz"
                    else:
                      print counter

        except:
            print "\n[!] Please use whole numbers\n"