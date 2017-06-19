# coding=utf-8
"""
unit_converter.py
Plan:
Program greets user and describes what's the purpose of the program
Program asks user to enter number of kilometers.
User enters the amount of kilometers.
Program converts these kilometers into miles and prints them.
Program asks user if they'd want to do another conversion.
If yes, repeat the above process (except the greeting).
If not, program says goodbye and stops.

"""

if __name__ == '__main__':

    operator = ""
    units = ["km", "mi"]
    con_mikm = 0.621371
    con_kmmi = 1.60934

    print 45 * "-" + "\n" + 45 * "-" + "\n\nWelcome to the \'Unit Converter\'\n\n" + "This Program converts Kilometers\ninto Miles and vice versa\n\n" + 45 * "-"




    while True:
            value = ""
            unit = ""

            operator = raw_input(45 * "-" + "\n\nWhat would you like to do?\n\n Enter ......to convert\n Q ......Quit the program\n")

            if operator.lower() == "q":
                print 45 * "-" + "\n See you!\n" + 45 * "-"
                break

            else:
                while unit not in units:

                    unit = raw_input("\nEnter the unit you want to convert from: \n mi ......for miles\n km ......for kilometers\n")

                    if unit in units:
                            break
                    else:
                        print "[!] Please enter \"mi\" or \"km\"\n"



                while True:
                    try:
                        value = float(raw_input("Enter the distance in " + str(unit) + " you want to convert: \n"))

                        if unit == units[0]:
                            print value, unit, "is", float(value) * con_mikm, "miles\n"
                            break
                        elif unit == units[1]:
                            print value, unit, "is", float(value) * con_kmmi, "kilometers\n"
                            break
                    except:
                        print "[!] Please use numbers\n"






