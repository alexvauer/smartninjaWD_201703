# coding=utf-8
"""
9.3 (bonus): Forensics program
"""

# Suspects facts
suspects = {}

eva = {}
eva['Gender'] = "Female"
eva['Race'] = "White"
eva['Hair'] = "Blonde"
eva['Eyes'] = "Blue"
eva['Face'] = "Oval"
suspects['Eva']=eva

larisa = {}
larisa['Gender'] = "Female"
larisa['Race'] = "White"
larisa['Hair'] = "Brown"
larisa['Eyes'] = "Brown"
larisa['Face'] = "Oval"
suspects['Larisa'] = larisa

miha = {}
miha['Gender'] = "Male"
miha['Race'] = "White"
miha['Hair'] = "Black"
miha['Eyes'] = "Blue"
miha['Face'] = "Oval"
suspects['Miha'] = miha

matej = {}
matej['Gender'] = "Male"
matej['Race'] = "White"
matej['Hair'] = "Brown"
matej['Eyes'] = "Green"
matej['Face'] = "Square"
suspects['Matej'] = matej

# DNA strings

dna = {}
hair_color = {}
hair_color['Black'] = "CCAGCAATCGC"
hair_color['Brown'] = "GCCAGTGCCG"
hair_color['Blonde'] = "TTAGCTATCGC"
dna['Hair'] = hair_color

face = {}
face['Square'] = "GCCACGG"
face['Round'] = "ACCACAA"
face['Oval'] = "AGGCCTCA"
dna['Face'] = face

eyes = {}
eyes['Blue'] = "TTGTGGTGGC"
eyes['Green'] = "GGGAGGTGGC"
eyes['Brown'] = "AAGTAGTGAC"
dna['Eyes'] = eyes

gender = {}
gender['Female'] = "TGAAGGACCTTC"
gender['Male'] = "TGCAGGAACTTC"
dna['Gender'] = gender

race = {}
race['White'] = "AAAACCTCA"
race['Black'] = "CGACTACAG"
race['Asian'] = "CGCGGGCCG"
dna['Race'] = race



def suspectDNA(suspect):

    suspect_hair = suspects[suspect]['Hair']
    suspect_face = suspects[suspect]['Face']
    suspect_eyes = suspects[suspect]['Eyes']
    suspect_gender = suspects[suspect]['Gender']
    suspect_race = suspects[suspect]['Race']

    the_suspectDNA = []
    the_suspectDNA.append(dna['Hair'][suspect_hair])
    the_suspectDNA.append(dna['Face'][suspect_face])
    the_suspectDNA.append(dna['Eyes'][suspect_eyes])
    the_suspectDNA.append(dna['Gender'][suspect_gender])
    the_suspectDNA.append(dna['Race'][suspect_race])

    return the_suspectDNA


if __name__ == '__main__':
    print "hmmmmm"

