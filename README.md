# PCB Drilling Optimization Using PSO and Fuzzy Logic

## Project Overview
This project addresses the Traveling Salesman Problem (TSP) in the context of PCB drilling, aiming to optimize the sequence of drilling holes. By integrating Particle Swarm Optimization (PSO) with Fuzzy Logic, we developed an efficient algorithm to minimize the total drilling distance and improve the overall manufacturing process.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Libraries Used](#libraries-used)
- [Results](#results)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Introduction
In PCB manufacturing, optimizing the sequence of drilling holes is crucial to minimize time and wear on equipment. This project combines PSO and Fuzzy Logic to dynamically adjust the inertia weight during the optimization process, ensuring the best possible performance.

## Features
- **Particle Swarm Optimization (PSO)**:
  - Simulates a swarm of particles to explore and find the shortest route for drilling.
  - Dynamically updates positions and velocities of particles.
- **Fuzzy Logic**:
  - Adjusts the inertia weight (`w`) based on predefined membership functions.
  - Balances exploration and exploitation in PSO.
- **Visualization**:
  - Plots the graph of holes and the optimal drilling route.

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/pcb-drilling-optimization.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd pcb-drilling-optimization
   ```
3. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the main script**:
   ```bash
   python main.py
   ```
2. **View the results**:
   - The script prints the best route and its total distance.
   - Visualizations of the holes and the optimal route will be displayed.

## Libraries Used
- **NumPy**: For numerical operations.
- **Matplotlib**: For plotting graphs and visualizing routes.
- **SciKit-Fuzzy**: For implementing fuzzy logic control systems.
- **Random**: For generating random samples and simulating the stochastic nature of PSO.

## Results
- Significant reductions in total drilling distance were achieved.
- Visualizations clearly showed the optimized routes, validating the improvements.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.

## Acknowledgements
A huge thanks to our amazing team for their dedication and hard work on this project.
Hazem Medhat
Mohamed Ashraf
Jana Raafat
Mariam Mohamed


