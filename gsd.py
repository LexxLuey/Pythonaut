from ortools.linear_solver import pywraplp
def newSolver(name,integer=False):
    return pywraplp.Solver(name,\
                           pywraplp.Solver.
                           CBC_MIXED_INTEGER_PROGRAMMING \
                           if integer else \
                           pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

def solve_model(Part,Target,Cost,Inventory,D,SC,SL):
    s = newSolver('Multi-period soap blending problem')
    Oils= range(len(Part))
    Periods, Acids = range(len(Cost[0])), range(len(Part[0]))
    Buy = [[s.NumVar(0,D,'') for _ in Periods] for _ in Oils]
    Blnd = [[s.NumVar(0,D,'') for _ in Periods] for _ in Oils]
    Hold = [[s.NumVar(0,D,'') for _ in Periods] for _ in Oils]
    Prod = [s.NumVar(0,D,'') for _ in Periods]
    CostP= [s.NumVar(0,D*1000,'') for _ in Periods]
    CostS= [s.NumVar(0,D*1000,'') for _ in Periods]
    Acid = [[s.NumVar(0,D*D,'') for _ in Periods] for _ in Acids]
    for i in Oils:
        s.Add(Hold[i][0] == Inventory[i][0])
    for j in Periods:
        s.Add(Prod[j] == sum(Blnd[i][j] for i in Oils))
        s.Add(Prod[j] >= D)
        if j < Periods[-1]:
            for i in Oils:
                s.Add(Hold[i][j]+Buy[i][j]-Blnd[i][j] == Hold[i][j+1])
        s.Add(sum(Hold[i][j] for i in Oils) >= SL[0])
        s.Add(sum(Hold[i][j] for i in Oils) <= SL[1])
    for k in Acids:
        s.Add(Acid[k][j]==sum(Blnd[i][j]*Part[i][k] for i in Oils))
        s.Add(Acid[k][j] >= Target[0][k] * Prod[j])
        s.Add(Acid[k][j] <= Target[1][k] * Prod[j])
    s.Add(CostP[j] == sum(Buy[i][j] * Cost[i][j] for i in Oils))
    s.Add(CostS[j] == sum(Hold[i][j] * SC for i in Oils))
    Cost_product = s.Sum(CostP[j] for j in Periods)
    Cost_storage = s.Sum(CostS[j] for j in Periods)
    s.Minimize(Cost_product+Cost_storage)
    rc = s.Solve()
    B,L,H,A = SolVal(Buy),SolVal(Blnd),SolVal(Hold),SolVal(Acid)
    CP,CS,P = SolVal(CostP),SolVal(CostS),SolVal(Prod)
    return rc,ObjVal(s),B,L,H,P,A,CP,CS

