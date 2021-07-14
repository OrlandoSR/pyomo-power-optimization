# Code for creating the lists given to Reusable.py from text files
# \t is tab and \n is new line
from io import StringIO
import csv
from Variables import *

path_to_line = "../res/4Bus/line.txt"
path_to_bus = "../res/4Bus/bus.txt"
path_to_generator = "../res/4Bus/gen.txt"

with open(path_to_line) as f_line:
    linecontent = f_line.readlines()

with open(path_to_bus) as f_bus:
    buscontent = f_bus.readlines()

with open(path_to_generator) as f_gen:
    gencontent = f_gen.readlines()

# Recieves the list of string the original part to replace and the replacement return the modified list
def cleanList(list, orig, repl):
    result = []
    for i in list:
        result.append(i.replace(orig, repl))

    return result


buscontent = cleanList(buscontent, "\n", "")
buscontent = cleanList(buscontent, "\t", ",")

gencontent = cleanList(gencontent, "\n", "")
gencontent = cleanList(gencontent, "\t", ",")

linecontent = cleanList(linecontent, "\n", "")
linecontent = cleanList(linecontent, "\t", ",")

# Take the cleaned list of strings and create an appropiate object for each
# for each individual string in the list split at the
def buildBusList(bclist):
    busList = []
    paramList = []

    for i in bclist:
        f = StringIO(i)
        reader = csv.reader(f, delimiter=',')
        for j in reader:
            paramList.append(j)

    for i in paramList:
         busList.append(Bus(i[0], float(i[1])))

    return busList

def buildLineList(llist):
    lineList = []
    paramList = []

    for i in llist:
        f = StringIO(i)
        reader = csv.reader(f, delimiter=',')
        for j in reader:
            paramList.append(j)

    for i in paramList:
        lineList.append(Line(i[0], i[1], i[2], float(i[5]), float(i[3])))

    return lineList


def buildGenList(glist):
    genList = []
    paramList = []

    for i in glist:
        f = StringIO(i)
        reader = csv.reader(f, delimiter=',')
        for j in reader:
            paramList.append(j)

    for i in paramList:
        genList.append(Generator(i[0], i[1], float(i[2]), float(i[3]), float(i[4])))

    return genList


busList = buildBusList(buscontent)
lineList = buildLineList(linecontent)
genList = buildGenList(gencontent)

for i in range(len(busList)):
    print(f"Bus: ID = {busList[i].ID}, Load = {busList[i].load}")

for i in range(len(lineList)):
    print(f"Line: ID = {lineList[i].ID}, Input bus = {lineList[i].inputBus}, Output bus = {lineList[i].outputBus}, Capacity = {lineList[i].capacity}, Susceptance = {lineList[i].susceptance}")

for i in range(len(genList)):
    print(f"Generator: ID = {genList[i].ID}, Location Bus = {genList[i].locationBus}, Cost = {genList[i].cost}, Max = {genList[i].outputMaximum}, Min = {genList[i].outputMinimum}")
