# coding=utf-8

class Vehicle(object):
    def __init__(self,brand, model, km, service_date):
        self.brand = brand
        self.model = model
        self.km = km
        self.service_date = service_date

    def show(self):
        print"Brand: {}\nModel:{}\nKm:{}\nservice date:{}\n".format(self.brand, self.model, self.km, self.service_date)

if __name__ == '__main__':

    with open("vehicles.txt", "r") as v:

        lines = v.readlines()

        allVehicles = []
        for line in lines:
            line = line.strip("\n")
            brand2, model2, km2, service_date2 = line.split(",")
            vehicle2 = Vehicle(brand2,model2,km2,service_date2)


            print new_dict['Date'], " . ", new_dict['Menü'], " . . . ", new_dict['Preis'], " €"

            allVehicles.append(vehicle2)

    AllVehicles = [
        Vehicle("Audi", "A5", "12444", "2017.01.17"),
        Vehicle("Renault", "Escapce", "344245", "2017.03.18")
        ]

    print 45 * "-" + "\nWillkommen beim Vehicle Manager\n" + 45 * "-"

    while True:
        answer = raw_input("\nWas möchtest du machen?\n"
                           "(1) Alle Fahrzeuge anzeigen\n"
                           "(2) Fahrzeug hinzufügen\n"
                           "(3) Kilometerstand editieren\n"
                           "(4) Service Datum editieren\n"
                           "(q) Programm verlassen\n")

        if answer.lower() == "q":
            break

        elif answer == "1":
            print 45 * "-" +"\nAlle Fahrzeuge im Fuhrpark:\n"

            for vehicle in vehicles:
                for speise,info in menus_dict.iteritems():

                    print speise, info

            print
            print "*" * 30

        elif answer == "2":

            print "\nSet hinzufügen"
            print "*"*30

            menuset = dict()
            speisentypen = ("Vorspeise","Hauptspeise","Nachsspeise")

            for speise in speisentypen:

                name = raw_input("Was ist der Name der {}?".format(speise))
                preis = raw_input("Was kostet die {}?".format(speise))

                menuset[speise] = (name, preis)

            tagesmenus.append(menuset)

        elif answer == "3":
            # todo: Schreibe Menü in File
            print "Set in file schreiben\n"
            content = "Speisentyp, Speise, Preis\n"
            for menus_dict in tagesmenus:
                for speise, info in menus_dict.iteritems():
                    content += "{},{},{}\n".format(speise,str(info[0]),str(info[1]))

            with open("menukarte.txt","w") as f:
                f.write(content)


        elif answer == "4":

            # todo: set löschen
            print "Set löschen\n"


        elif answer == "5":

            print "File lesen\n"
            with open("menukarte.txt","r") as f:

                lines = f.readlines()
                # Oder mit: lines = f.read().split("\n) <= gleiches ergebnis

            new_dict = dict()
            for line in lines[1:]:
                line = line.strip("\n")
                speisentyp2, name2, preis2 = line.split(",")
                new_dict[speisentyp2] = (name2,preis2)
            tagesmenus.append(new_dict)



        else: "Unknown Input...\n"

    print "Exit Restaurant Program\n"