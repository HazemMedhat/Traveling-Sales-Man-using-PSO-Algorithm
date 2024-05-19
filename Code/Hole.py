class Hole:
    """
    A class representing a hole in the Particle Swarm Optimization (PSO) algorithm for the Traveling Salesman Problem (TSP).

    Attributes:
        x [int]: The x-coordinate of the hole.
        y [int]: The y-coordinate of the hole.
    """
    def __init__(self, x:float , y:float) -> None:
        """
        Initialize a new Hole instance.

        Args:
            x [float]: The x-coordinate of the hole.
            y [float]: The y-coordinate of the hole.
        """
        self.x = x
        self.y = y