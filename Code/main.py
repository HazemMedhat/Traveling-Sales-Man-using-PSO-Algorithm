
from TSP import *
from PSO import *
from Fuzzy import *
if __name__ == "__main__":
    num_of_holes = 20
    num_particles = 20
    fuzzification = Fuzzification()
    w = fuzzification.simulate()
    max_iter = 100
    c1 = 1.5
    c2 = 2.5
    start_hole = 0  # Define the starting hole

    tsp_problem = TSP_Problem(num_of_holes)
    tsp_problem.plot_graph()

    pso = PSO(num_particles, num_of_holes, w, c1, c2, tsp_problem, start_hole)

    best_route, best_fitness = pso.run(max_iter)

    print("Best Route:", best_route)
    print("Best Fitness (Total Distance):", best_fitness)

    tsp_problem.plot_route(best_route)

