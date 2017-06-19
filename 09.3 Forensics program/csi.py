# coding=utf-8
from suspects import suspectDNA
"""
9.3 (bonus): Forensics program
"""
thesuspects = ['Eva','Miha','Matej','Larisa']
result = {}

if __name__ == '__main__':

    with open("dna.txt", "r") as factDNA:
        abuserDNA = factDNA.read()
        factDNA.close()


    for suspect in thesuspects:
        the_suspectDNA = suspectDNA(suspect)
        print "\n\nTesting - - - ",suspect, ": DNA-snippets: ",the_suspectDNA

        test = 0

        for item in the_suspectDNA:
            if abuserDNA.find(item) != -1:
                test += 1
                print item, ": match"
            else:
                print item, ": is not matching"

        result[suspect] = test

    print 45 * "-"
    print "\n"
    for suspect in thesuspects:

        if result[suspect] < 5:
            print "{} is not guilty".format(suspect)

        elif result[suspect] == 5:
            print "{} is guilty".format(suspect)

        else:
            print "nobody is guilty"


    print "\n"
    print 45 * "-"


