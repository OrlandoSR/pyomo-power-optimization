from pyomo.environ import *
from Variables import *

# create bus, gens, and lines
# later this will be done automatically from a txt file
busList = []
busList.append(Bus(1, 0))

lineList = []
lineList.append(Line(1, 1, 3, 50.0))

genList = []
genList.append(Generator(1, 1, 70.0, 0.0, 30.0))
genList.append(Generator(2, 1, 80.0, 0.0, 50.0))

# create model
model = ConcreteModel()

# declare decision variables

# generators
# finds bounds for the given object
def fb(model, i):
    return i.getBounds()


# create the set of generators from the list of generator objects
model.genSet = Set(initialize=genList)
# create the generator variables from the set of generators and assign the bounds using the find bounds function
model.Generators = Var(model.genSet, bounds=fb)


# debugging
# print(genList[0].ID)
# print(genList[1].ID)
