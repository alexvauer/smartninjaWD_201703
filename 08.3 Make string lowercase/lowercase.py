# coding=utf-8
"""
Homework 8.3: Make string lowercase
"""

operator = ""
operators = ["yes","no"]

if __name__ == '__main__':


    while operator not in operators:

        operator = raw_input(
        45 * "-" + "\n\nWould you like to Enter?\n\nPlease enter Yes or No?")

        if operator.lower() == operators[0]:
            print 45 * "-" + "\n Hey!\n" + 45 * "-"
            break

        elif operator.lower() == operators[1]:
            print 45 * "-" + "\n See you!\n" + 45 * "-"
            break
        else:
            print "\n[!] Please enter a valid string!\n"