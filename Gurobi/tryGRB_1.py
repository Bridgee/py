from gurobipy import *

m = Model('try')

x = m.addVar(ub=1.0, name='x')
y = m.addVar(ub=1.0, name='y')
z = m.addVar(ub=1.0, name="z")

obj = x*x + x*y + y*y + y*z + z*z + 2*x
m.setObjective(obj)

m.addConstr(x + 2 * y + 3 * z >= 4, "c0")
m.addConstr(x + y >= 1, "c1")

# Continuous Mode
m.optimize ()
for v in m.getVars ():
    print('%s %g' % (v.varName , v.x))
print('Obj: %g' % obj.getValue ())
m.write('tryGRB_1C.sol')

# Integer Mode
x.vType = GRB.INTEGER
y.vType = GRB.INTEGER
z.vType = GRB.INTEGER

m.optimize ()
for v in m.getVars ():
    print('%s %g' % (v.varName , v.x))
print('Obj: %g' % obj.getValue ())
m.write('tryGRB_1I.sol')

# Binary Mode
x.vType = GRB.BINARY
y.vType = GRB.BINARY
z.vType = GRB.BINARY

m.optimize ()
for v in m.getVars ():
    print('%s %g' % (v.varName , v.x))
print('Obj: %g' % obj.getValue ())
m.write('tryGRB_1B.sol')