import matplotlib.pyplot as plt
import numpy as np
from pymoo.visualization.scatter import Scatter
from agents import Household, Firm
from pymoo.algorithms.moo.nsga2 import NSGA2
from cge import CGE
from pymoo.termination import get_termination
from pymoo.optimize import minimize


def main():

    #SOLVER

    cge = CGE()
    algorithm = NSGA2()
    termination = get_termination('n_gen', 300)
    res = minimize(cge, algorithm, verbose=True, termination=termination)
    X = res.X
    F = res.F

    approx_ideal = F.min(axis=0)
    approx_nadir = F.max(axis=0)

    nF = (F - approx_ideal) / (approx_nadir - approx_ideal)

    fl = nF.min(axis=0)
    fu = nF.max(axis=0)
    print(f"Scale f1: [{fl[0]}, {fu[0]}]")
    print(f"Scale f2: [{fl[1]}, {fu[1]}]")

    plt.figure(figsize=(7, 5))
    plt.scatter(nF[:, 0], nF[:, 1], s=30, facecolors='none', edgecolors='blue')
    plt.title("Objective Space")
    plt.show()
    plt.savefig('C:/Users/joaco/Pictures/pareto.png')

if __name__ == '__main__':

    main()