from random import random



spaceCount = 272247
charCount = 1024977
spaceProb = spaceCount/(charCount)

f = open("stress.txt", "r")
line = f.readline()
fileOut = open("endFile.txt", "w")
while line!='':

    lineOut = ""
    for letter in line:
        if letter != " " and letter != "\'":
            if random() < spaceProb:
                lineOut += letter + " "
            else:
                lineOut += letter

    fileOut.write(lineOut)
    line = f.readline()