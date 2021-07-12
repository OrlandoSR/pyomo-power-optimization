from pyomo.environ import *
from Variables import *

baseMVA = 100

# create bus, gens, lines and angles
# later this will be done automatically from a txt file
busList = []
busList.append(Bus(1, 0))
busList.append(Bus(2, 0))
busList.append(Bus(3, 90))

lineList = []
lineList.append(Line(1, 1, 3, 50.0, 10))
lineList.append(Line(2, 1, 2, 50.0, 10))
lineList.append(Line(3, 2, 3, 50.0, 10))

genList = []
genList.append(Generator(1, 1, 70.0, 0.0, 30.0))
genList.append(Generator(2, 2, 80.0, 0.0, 50.0))

# construct list of angles it depends on the numbers of buses
# for each bus i need an angle
anglesList = []
# sets the ID for the angle that will be treated as reference
referenceID = 1
for i in busList:
    if i.ID == referenceID:
        anglesList.append(Angle(i.ID, 0, 0))
    else:
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

# Constraints
# reference angle is handled by the angle list generator
# each line needs a constraint that defines the values
# based on the power flow equation
# this list will contain
model.PowerFlowCon = ConstraintList()

# iterates through each line in the model to create its constraint with the power flow equation
for i in model.Lines:
    inbusid = i.inputBus
    outbusid = i.outputBus
    # the angle variables in the model for the input bus and output bus
    thetain = None
    thetaout = None

    # iterates through angles in the model to find the angles belonging to the specific line
    for j in model.Angles:
        if j.ID == inbusid:
            thetain = model.Angles[j]
        elif j.ID == outbusid:
            thetaout = model.Angles[j]

    model.PowerFlowCon.add(expr=model.Lines[i] == -i.susceptance * baseMVA * (thetain - thetaout))

# For each bus the input needs to equal the output
# this are the power conservation constraints
model.BalanceCon = ConstraintList()

# iterate through each bus from the given list (buses are not variables in model)
for i in busList:
    PowerBalance = 0
    # For each generator going in add to the power balance
    for j in model.Generators:
        # If the generator is at bus i then add that to the power of the bus
        if j.locationBus == i.ID:
            PowerBalance += model.Generators[j]

    # Check each line and if its output bus is bus i, add the line power to the power balance
    # If its input bus is bus i subtract the line power from the power balance
    for k in model.Lines:
        if k.outputBus == i.ID:
            PowerBalance += model.Lines[k]
        elif k.inputBus == i.ID:
            PowerBalance -= model.Lines[k]
    PowerBalance -= i.load
    model.BalanceCon.add(expr=PowerBalance == 0)


# debugging
# print(genList[0].ID)
# print(genList[1].ID)
# print(lineList[0].getBounds())
# print(f'{TotalCost}')
# for i in model.PowerFlowCon:
#    model.PowerFlowCon[i].pprint()
# for i in model.BalanceCon:
#    model.BalanceCon[i].pprint()
# model.BalanceCon.pprint()
