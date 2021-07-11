from pyomo.environ import *
from Variables import *

# create bus, gens, lines and angles
# later this will be done automatically from a txt file
busList = []
busList.append(Bus(1, 0))
busList.append(Bus(2, 0))
busList.append(Bus(3, 90))

lineList = []
lineList.append(Line(1, 1, 3, 50.0))
lineList.append(Line(2, 1, 2, 50.0))
lineList.append(Line(3, 2, 3, 50.0))

genList = []
genList.append(Generator(1, 1, 70.0, 0.0, 30.0))
genList.append(Generator(2, 1, 80.0, 0.0, 50.0))

# construct list of angles it depends on the numbers of buses
# for each bus i need an angle
anglesList = []
for i in busList:
    anglesList.append(Angle(i.ID, -1, 1))

# create model
model = ConcreteModel()

# declare decision variables
# finds bounds for the given object
def fb(model, i):
    # print(i.getBounds())
    return i.getBounds()


# generators
# create the set of generators from the list of generator objects
model.genSet = Set(initialize=genList)
# create the generator variables from the set of generators and assign the bounds using the find bounds function
model.Generators = Var(model.genSet, bounds=fb)

# line variables
# create the set of lines from the list given
model.lineSet = Set(initialize=lineList)
# create line variables from the set of lines
model.Lines = Var(model.lineSet, bounds=fb)

# phase angles
# create a set of angles from list given
model.anglesSet = Set(initialize=anglesList)
# create the angle variables from set given
model.Angles = Var(model.anglesSet, bounds=fb)

# Objective
# initialize an expression to hold the objective function
TotalCost = 0
# iterate through the list of generator and multiple them by their cost
for i in model.Generators:
    # print(i)
    TotalCost += i.cost*model.Generators[i]

# declare objective function inside the model
model.obj = Objective(expr=TotalCost)

# debugging
# print(genList[0].ID)
# print(genList[1].ID)
# print(lineList[0].getBounds())
# print(f'{TotalCost}')
