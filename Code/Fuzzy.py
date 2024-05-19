import numpy as np
import random
import skfuzzy as fuzz
from skfuzzy import control as ctrl

class Fuzzification:
    """
        A class to perform fuzzification of a Inertia weight .
    """
    def __init__(self, num_simulations=5):
        """
            Initialize the Fuzzification object.

            Args:
                num_simulations (int, optional): The number of simulations to run. Defaults to 5.
        """
        self.num_simulations = num_simulations
        self.wight_universe = np.arange(0.1, 2, 0.1)
        self.W = ctrl.Antecedent(self.wight_universe, 'Stability')

        self.W['not stable'] = fuzz.trimf(self.W.universe, [0.1, 0.1, 0.9])
        self.W['stable'] = fuzz.trimf(self.W.universe, [0.1, 0.9, 2])
        self.W['poor'] = fuzz.trimf(self.W.universe, [0.9, 2, 2])

    def simulate(self):
        """
            Run the fuzzification simulation.

            Returns:
                float: The average denazified weight.
        """
        denazified_Wights = []
        for _ in range(self.num_simulations):
            while True:
                crisp = random.uniform(0.1, 2)
                u = fuzz.interp_membership(self.W.universe, self.W['stable'].mf, crisp)
                alpha = np.random.uniform(0, 1)
                if alpha <= u:
                    denazified_Wights.append(crisp)
                    break
        return np.mean(denazified_Wights)