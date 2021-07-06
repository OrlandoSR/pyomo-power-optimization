from pyomo.environ import *

# create model
model = ConcreteModel()

# declare decision variables

# generators
model.P1 = Var(bounds=(0.0, 70.0))
model.P2 = Var(bounds=(0.0, 80.0))

# line variables
model.F13 = Var(bounds=(-50.0, 50.0))
model.F12 = Var(bounds=(-50.0, 50.0))
model.F23 = Var(bounds=(-50.0, 50.0))

# phase angles
model.theta1 = Var(bounds=(-.6, 0.6))
model.theta2 = Var(bounds=(-0.6, 0.6))
model.theta3 = Var(bounds=(-0.6, 0.6))

# Objective
model.obj = Objective(expr=30*model.P1 + 50*model.P2, sense=minimize)

# Constraints
model.refBus = Constraint(expr=model.theta1 == 0)
model.F13_Con = Constraint(expr=model.F13 == -10.0*100*(model.theta3 - model.theta1))
model.F12_Con = Constraint(expr=model.F12 == -10.0*100*(model.theta2 - model.theta1))
model.F23_Con = Constraint(expr=model.F23 == -10.0*100*(model.theta3 - model.theta2))

model.Conserve1 = Constraint(expr=model.P1 - model.F13 - model.F12 == 0)
model.Conserve2 = Constraint(expr=model.P2 + model.F12 - model.F23 == 0)
model.Conserve3 = Constraint(expr=model.F13 + model.F23 == 100)

# Solve
results = SolverFactory('glpk').solve(model)
results.write()

# Debugging
# print('\n[Debugging]')
# model.display()

# Display Solution
print('\nObjective = ', model.obj())

print('P1 = ', model.P1())
print('P2 = ', model.P2())

print('F12 = ', model.F12())
print('F13 = ', model.F13())
print('F23 = ', model.F23())
print('Theta1 =', model.theta1())
print('Theta2 =', model.theta2())
print('Theta3 =', model.theta3())
