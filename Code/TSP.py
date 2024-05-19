import random
import matplotlib.pyplot as plt

from Hole import *

class TSP_Problem:
    """
    A class representing the Traveling Salesman Problem (TSP) for PCB drilling.

    Attributes:
        num_holes [int]: The number of holes in the PCB.
        holes list[Hole]: A list of Hole instances representing the holes in the PCB.
        distances Dic{}: A dictionary containing the distances between each pair of holes.
    """
    def __init__(self, num_holes:int) -> None:
        """
        Initialize a new TSPProblem instance.

        Args:
            num_holes: The number of holes in the PCB.
        """
        self.num_holes = num_holes
        self.holes = self.initialize_holes()
        self.distances = self.calc_distances()

    def initialize_holes(self) -> list[Hole]:
        """
        Initialize the holes in the PCB.

        Returns:
            A list of Hole instances representing the holes in the PCB.
        """
        return [Hole(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(self.num_holes)]

    def calc_distances(self) -> dict:
        """
        Calculate the distances between each pair of holes.

        Returns:
            A dictionary containing the distances between each pair of holes.
        """
        distances = {}
        for i in range(self.num_holes):
             for j in range(i +1, self.num_holes):
                #Euclidean distance
                distance = ((self.holes[i].x - self.holes[j].x)**2 + (self.holes[i].y - self.holes[j].y)**2)**0.5
                # Map the disctance between 2 holes
                distances[f"{i}-{j}"] = distance
                distances[f"{j}-{i}"] = distance
        return distances

    def plot_graph(self) -> None:
        """
        Plot the graph of the holes and their distances.
        """
        plt.figure(figsize=(8, 6))
        for i, hole in enumerate(self.holes):
            plt.plot(hole.x, hole.y, 'o', markersize=15, markerfacecolor='black', markeredgewidth=2)
            plt.text(hole.x + 2, hole.y + 2, f"Hole {i+1}", fontsize=12)
        for key, distance in self.distances.items():
            start, end = key.split('-')
            start_x = self.holes[int(start)].x
            start_y = self.holes[int(start)].y
            end_x = self.holes[int(end)].x
            end_y = self.holes[int(end)].y
            plt.plot([start_x, end_x], [start_y, end_y], 'b-', alpha=0.7)
            plt.text((start_x + end_x) / 2, (start_y + end_y) / 2, f"{distance:.2f}", ha='center', va='center', fontsize=10)
        plt.xlabel('X-coordinate')
        plt.ylabel('Y-coordinate')
        plt.title('PCB Drilling Problem - Sample Visualization')
        plt.axis('equal')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

    def route_cost(self, route:list[int])-> float:
        """
        Calculate the total distance of a given route.

        Args:
            route list[int]: A list of hole indices representing the route.

        Returns:
            The total distance of the given route.
        """
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distances[f"{route[i]}-{route[i+1]}"]
        return total_distance

    def plot_route(self, route:list[int]) -> None:
        """
        Plot the route on the graph of the holes.

        Args:
            route list[int]: A list of hole indices representing the route.
        """
        total_dsi = 0
        x_coords = [hole.x for hole in self.holes]
        y_coords = [hole.y for hole in self.holes]
        route_x_coords = [x_coords[i] for i in route]
        route_y_coords = [y_coords[i] for i in route]
        plt.figure(figsize=(8, 6))
        plt.scatter(x_coords, y_coords, color='blue', label='Holes')
        plt.plot(route_x_coords, route_y_coords, color='red', linestyle='-', marker='o', label='Route')
        for i in range(len(route) - 1):
            start_index = route[i]
            end_index = route[i + 1]
            start_x = x_coords[start_index]
            start_y = y_coords[start_index]
            end_x = x_coords[end_index]
            end_y = y_coords[end_index]
            distance = self.distances[f"{start_index}-{end_index}"]
            annotation_x = (start_x + end_x) / 2
            annotation_y = (start_y + end_y) / 2 + 0.5
            plt.annotate(f"{distance:.2f}", (annotation_x, annotation_y), textcoords="offset points", xytext=(0, 5), ha='center')
            total_dsi += distance
        plt.text(0.5, 0.95, f"Total Distance: {total_dsi:.2f}", transform=plt.gca().transAxes, ha='center', va='center')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Best Route')
        plt.legend()
        plt.grid(True)
        plt.show()