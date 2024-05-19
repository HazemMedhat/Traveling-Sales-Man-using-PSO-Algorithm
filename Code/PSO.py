import numpy as np
from TSP import *

class PSO:
    """
    A class representing the Particle Swarm Optimization (PSO) algorithm for the Traveling Salesman Problem (TSP).

    Attributes:
        num_particles: The number of particles in the PSO population.
        num_cities: The number of cities in the TSP.
        w: The inertia weight for the PSO algorithm.
        c1: The cognitive coefficient for the PSO algorithm.
        c2: The social coefficient for the PSO algorithm.
        tsp_problem: A TSPProblem instance representing the TSP problem.
        start_hole: The index of the starting hole in the TSP problem.
        particles: A list of lists representing the positions of the particles in the PSO population.
        velocities: A list of lists representing the velocities of the particles in the PSO population.
        pbest: A list of lists representing the personal best positions of the particles in the PSO population.
        pbest_fitness: A list of floats representing the personal best fitness values of the particles in the PSO population.
        gbest: A list representing the global best position in the PSO population.
        gbest_fitness: A float representing the global best fitness value in the PSO population.
    """
    def __init__(self, num_particles:int , num_cities:int , w:float , c1:float , c2:float , tsp_problem:TSP_Problem, start_hole:int) -> None:
        """
        Initialize a new PSO instance.

        Args:
            num_particles int: The number of particles in the PSO population.
            num_cities int: The number of cities in the TSP.
            w float: The inertia weight for the PSO algorithm.
            c1 float: The cognitive coefficient for the PSO algorithm.
            c2 float: The social coefficient for the PSO algorithm.
            tsp_problem TSP_Problem: A TSPProblem instance representing the TSP problem.
            start_hole int: The index of the starting hole in the TSP problem.
        """
        self.num_particles = num_particles
        self.num_cities = num_cities
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.tsp_problem = tsp_problem
        self.start_hole = start_hole
        self.particles = self.initialize_particles()
        self.velocities = self.initialize_velocity()
        self.pbest = self.particles[:]
        self.pbest_fitness = [self.calculate_fitness(p) for p in self.particles]
        self.gbest = self.particles[np.argmin(self.pbest_fitness)]
        self.gbest_fitness = min(self.pbest_fitness)

    def initialize_particles(self) -> list[list[int]]:
        """
        Initialize the positions of the particles in the PSO population.
        The initial positions of all particles in the PSO population.
        Each particle is a list of cities, representing a permutation of cities to visit.

        Returns:
            A list of lists representing the positions of the particles in the PSO population.
        """
        particles = []
        for _ in range(self.num_particles):
            particle = random.sample(range(self.num_cities), self.num_cities)
            particle.remove(self.start_hole)
            particle = [self.start_hole] + particle + [self.start_hole]
            particles.append(particle)
        return particles

    def initialize_velocity(self) -> list[list[tuple[int]]]:
        """
        Initialize the velocities of the particles in the PSO population.

        Returns:
            A list of tuple representing the velocities of the particles in the PSO population.
        """
        velocities = [[(random.randint(1, self.num_cities-2), random.randint(1, self.num_cities-2)) for _ in range(self.num_cities)] for _ in range(self.num_particles)]
        return velocities

    def calculate_fitness(self, route:list[int]) -> float:
        """
        Calculate the fitness of a given route.

        Args:
            route: A list of hole indices representing the route.

        Returns:
            The total distance of the given route.
        """
        return self.tsp_problem.route_cost(route)

    def update_velocity(self, particle:list[int], velocity:list[tuple[int]], pbest:list[int], gbest:list[int]) -> list :
        """
        Update the velocity of a particle.

        Args:
            particle: A list of hole indices representing the position of the particle.
            velocity: A list of tuple representing the velocity of the particle.
            pbest: A list of hole indices representing the personal best position of the particle.
            gbest: A list of hole indices representing the global best position in the PSO population.

        Returns:
            A list of tuples representing the updated velocity of the particle.
        """
        new_velocity = []
        for swap in velocity:
            if random.random() < self.w:
                new_velocity.append(swap)
        for _ in range(len(particle) - 2):
            if random.uniform(0,4) < self.c1:
                swap = (pbest[random.randint(1, len(particle)-2)], pbest[random.randint(1, len(particle)-2)])
                new_velocity.append(swap)
            elif random.uniform(0,4) < self.c2:
                swap = (gbest[random.randint(1, len(particle)-2)], gbest[random.randint(1, len(particle)-2)])
                new_velocity.append(swap)
        return new_velocity

    def update_position(self, particle:list[int], velocity:list[tuple[int]]) ->list[int] :
        """
        Update the position of a particle.

        Args:
            particle: A list of hole indices representing the position of the particle.
            velocity: A list of tuples representing the velocity of the particle.

        Returns:
            A list of hole indices representing the updated position of the particle.
        """
        new_position = particle.copy()
        for swap in velocity:
            i, j = swap
            new_position[i], new_position[j] = new_position[j], new_position[i]
        return new_position

    def run(self, max_iter:int) -> tuple:
        """
        Run the PSO algorithm for a given number of iterations.

        Args:
            max_iter: The maximum number of iterations for the PSO algorithm.

        Returns:
            A tuple containing the global best position and the global best fitness value.
        """
        for _ in range(max_iter):
            for i in range(self.num_particles):
                self.velocities[i] = self.update_velocity(self.particles[i], self.velocities[i], self.pbest[i], self.gbest)
                self.particles[i] = self.update_position(self.particles[i], self.velocities[i])
                current_fitness = self.calculate_fitness(self.particles[i])
                if current_fitness < self.pbest_fitness[i]:
                    self.pbest[i] = self.particles[i]
                    self.pbest_fitness[i] = current_fitness
                    if current_fitness < self.gbest_fitness:
                        self.gbest = self.particles[i]
                        self.gbest_fitness = current_fitness
        return self.gbest, self.gbest_fitness