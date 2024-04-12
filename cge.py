import numpy as np
from pymoo.core.problem import ElementwiseProblem
from pymoo.util.misc import stack

class CGE(ElementwiseProblem):

    def __init__(self):
        super().__init__(n_var=8,
                         n_obj=3,
                         n_constr=4,
                         xl=np.array([0, 0, 0, 0, 0, 0, 0, 0]),
                         xu=np.array([100, 75, 100, 75, 100, 100, 100, 100]))

    def _evaluate(self, x, out, *args, **kwargs):

        f1 = -1 * (((x[0] ** 0.3) * (x[1] ** 0.7)) + ((x[2] ** 0.2) * (x[3] ** 0.8)))

        f2 = ((x[4] ** 0.6) * (x[5] ** 0.4))
        f3 = ((x[6] ** 0.1) * (x[7] ** 0.9))

        g1 = (x[4] + x[6]) - 100
        g2 = (x[5] + x[7]) - 75
        g3 = (x[0] + x[2]) - ((x[4] ** 0.6) * (x[5] ** 0.4))
        g4 = (x[1] + x[3]) - ((x[6] ** 0.1) * (x[7] ** 0.9))

        out['F'] = [f1, f2, f3]
        out['G'] = [g1, g2, g3, g4]
