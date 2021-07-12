class Bus:
    def __init__(self, id, load):
        self.ID = id
        self.load = load

    ID = None
    load = 0


class Line:
    def __init__(self, id, inputbus, outputbus, cap, suscept):
        self.ID = id
        self.inputBus = inputbus
        self.outputBus = outputbus
        self.capacity = cap
        self.susceptance = suscept

    ID = None
    inputBus = None
    outputBus = None
    susceptance = 0
    capacity = None

    def getBounds(self):
        return (-self.capacity, self.capacity)


class Generator:
    def __init__(self, id, locationbus, outputmax, outputmin, cost):
        self.ID = id
        self.locationBus = locationbus
        self.outputMaximum = outputmax
        self.outputMinimum = outputmin
        self.cost = cost

    ID = None
    locationBus = None
    outputMaximum = 0
    outputMinimum = 0
    cost = 0

    def getBounds(self):
        return (self.outputMinimum, self.outputMaximum)


class Angle:
    def __init__(self, id, lb, ub):
        self.ID = id
        self.lb = lb
        self.ub = ub

    ID = None
    lb = -1
    ub = 1

    def getBounds(self):
        return (self.lb, self.ub)
