# coding=utf-8
from datetime import date
"""
Exercise 9.2: Restaurant menu
"""



if __name__ == '__main__':

    tagesmenus = []

    print "Bisherige Tagesmenüs:"
    with open("menukarte.txt", "r") as menufile:

        lines = menufile.readlines()

    new_dict = dict()
    for line in lines:

        line = line.strip("\n")
        datum2, essen2, preis2 = line.split(",")
        new_dict = {}
        new_dict['Menü'] = essen2
        new_dict['Preis'] = preis2
        new_dict['Date'] = datum2

        print new_dict['Date']," . ",new_dict['Menü'], " . . . ",  new_dict['Preis'], " €"

        tagesmenus.append(new_dict)

    while True:
        menu ={}
        essen = raw_input("\nWas ist das heutige Tagesmenü?\n")

        while True:
            try:
                preis = float(raw_input("Wieviel kostet das Tagesmenü?\n"))
                break

            except:
                print "\nGib einen Preis in Zahlen an"


        menu['Menü'] = essen
        menu['Preis'] = str(preis)
        menu['Date'] = date.today()

        tagesmenus.append(menu)
        counter = 0
        text = ""

        for item in tagesmenus:

            text += str(tagesmenus[counter]['Date']) +","+ str(tagesmenus[counter]['Menü']) +","+ str(tagesmenus[counter]['Preis']) + "\n"
            counter += 1


        with open("menukarte.txt", "w+") as menufile:
            menufile.write(text)

            menufile.close()  # close the TXT file

        print "Neues Menü...", menu['Menü'] ,"  hinzugefügt\nBis morgen!\n" + 45 * "-"
        break

