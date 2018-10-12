from gurobipy import *

m = Model('try')

x = m.addVar(vtype=GRB.BINARY, name='x')
y = m.addVar(vtype=GRB.BINARY, name='y')

m.setObjective(x+2*y, GRB.MAXIMIZE)

m.addConstr(x+y>=1, 'c0')

m.optimize()

if m.status == GRB.Status.INF_OR_UNBD:
    # Turn presolve off to determine whether model is infeasible
    # or unbounded
    m.setParam(GRB.Param.Presolve, 0)
    m.optimize()

if m.status == GRB.Status.OPTIMAL:
    print('Optimal objective: %g' % m.objVal)
    m.write('tryGRB_0.sol')
    exit(0)
elif m.status != GRB.Status.INFEASIBLE:
    print('Optimization was stopped with status %d' % m.status)
    exit(0)


# Model is infeasible - compute an Irreducible Inconsistent Subsystem (IIS)

print('')
print('Model is infeasible')
m.computeIIS()
m.write("model.ilp")
print("IIS written to file 'model.ilp'")