# coding=utf-8

class Vehicle(object):
    def __init__(self,brand, model, km, service_date):
        self.brand = brand
        self.model = model
        self.km = km
        self.service_date = service_date

    def show(self):
        print"Brand: {}\nModel:{}\nKm:{}\nservice date:{}\n".format(self.brand, self.model, self.km, self.service_date)

    def stringer(self):
        string = "{},{},{},{}\n".format(self.brand,self.model,self.km,self.service_date)
        return string

    def showinline(self):
        string = "Brand: {} | Model:{} | Km:{} | service date:{}".format(self.brand, self.model, self.km, self.service_date)
        return string

    def edit(self,km2,date2):

        if km2:
            self.km = km2

        if date2:
            self.service_date = date2



if __name__ == '__main__':

    with open("vehicles.txt", "r") as v:

        lines = v.readlines()

        AllVehicles = []
        for line in lines:
            line = line.strip("\n")
            brand2, model2, km2, service_date2 = line.split(",")
            vehicle2 = Vehicle(brand2, model2, km2, service_date2)

            AllVehicles.append(vehicle2)

    print 40 * "-" + "\nWelcome to the Vehicle manager\n"+40 * "-"+"\n"

    while True:

        answer = raw_input("Please select an option\n"
                  "(1) Show vehicles\n"
                  "(2) Edit vehicle\n"
                  "(3) Add vehicle\n"
                  "(q) Quit program\n")

        if answer.lower() == "q":
            # save cars list to file

            text = ""
            for Item in AllVehicles:

                text+= Item.stringer()


            with open("vehicles.txt", "w+") as v2:
                v2.write(text)

                v2.close()  # close the TXT file

            print "\n" +40 * "-" +"\nExiting program..."
            break

        elif answer == "1":
            for x in AllVehicles:
                print x.showinline()

            print ""
        elif answer == "2":
            print "\nEdit vehicle:\n\nWhich Vehicle you want to edit?"

            list = []
            counter = 1
            for Item in AllVehicles:
                print "[{}]  {}".format(counter,Item.showinline())
                list.append(counter)
                counter +=1

            chooser = 0
            while chooser not in list:
                try:
                    chooser = int(raw_input("\nPlease enter the vehicle number:\n"))
                    if chooser not in list:
                        print "[!] Please enter a valid vehicle number\n"
                except:
                    print "[!] Please enter a valid vehicle number\n"


            print "\n",[chooser]," ", AllVehicles[chooser-1].showinline()

            new_km = raw_input("Please enter the new km:\n")
            new_service_date = raw_input("Please enter a the new service date:\n")
            AllVehicles[chooser-1].edit(new_km,new_service_date)

            print ("Edited vehicle:\n{}\n".format(AllVehicles[chooser-1].showinline()))



        elif answer == "3":
            print "\nAdding Vehicle..."
            brand = raw_input(" Please enter the brand of the new vehicle:\n")
            model = raw_input(" Please enter the model of the new vehicle:\n")
            km = raw_input(" Please enter the km of the new vehicle:\n")
            service_date = raw_input(" Please enter the service date of the new vehicle:\n")

            my_vehicle = Vehicle(brand,model,km,service_date)
            AllVehicles.append(my_vehicle)

            print "Vehicle added to list"







        else:
            print "\nPlease check yout input, and try again"