from __future__ import print_function
from ortools.linear_solver import pywraplp #loads the Python wrapper of the linear programming subset of OR-Tools
def solve_coexistence():
    t = 'Amphibian coexistence' 
    s = pywraplp.Solver(t,pywraplp.Solver.GLOP_LINEAR_PROGRAMMING) #names and creates a linear programming solver using Google’s own GLOP
    x = [s.NumVar(0, 1000,'x[%i]' % i) for i in range(3)] #create a one-dimensional array x of three decision variables that can take on values between 0 and 1000
    pop = s.NumVar(0,3000,'pop')
    s.Add(2*x[0] + x[1] + x[2] <= 1500)
    s.Add(x[0] + 3*x[1] + 2*x[2] <= 3000)
    s.Add(x[0] + 2*x[1] + 3*x[2] <= 4000)
    s.Add(pop == x[0] + x[1] + x[2])
    s.Maximize(pop)
    s.Solve()
    return pop.SolutionValue(),[e.SolutionValue() for e in x]
pop,x=solve_coexistence()
T=[['Specie', 'Count']]
for i in range(3):
    T.append([['Toads','Salamanders','Caecilians'][i], x[i]])
T.append(['Total', pop])
for e in T:
    print (e[0],e[1])
