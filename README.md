# Knowledge Representation for Stochastic Predator–Prey Dynamics: A Lion vs Deer Case Study
## Project Overview
This repository contains the source code for a Knowledge Representation and Reasoning (KRR) project exploring autonomous decision-making in a stochastic $8 \times 8$ grid world. The simulation pits a Predator (Lion) using a model-based Markov Decision Process (MDP) against a Prey (Deer) using a local heuristic look-ahead search.
## Key Features
* **MDP Solver**: Implements Value Iteration to account for environmental stochasticity.
* **Stochasticity**: Includes a 5% "movement slip" to test agent robustness.

* **Heuristic Reasoning**: Local search logic for the prey agent.

* **Visualization**: Real-time GUI/Console output showing agent movements and capture events.

## Project Structure
  The system is modularized into five primary files:
  * main.py: The entry point that manages the simulation loop and stamina constraints.
  * mdp_solver.py: Contains the Value Iteration algorithm and Bellman equation logic ($8^4$ state-space).
  * agents.py: Defines the Lion’s transition distribution and the Deer’s heuristic scoring function.
  * environment.py: Manages the $8 \times 8$ grid, random obstacle placement, and BFS-based reachability validation.
  * pygame_visualizer.py: Handles the graphical rendering, real-time stamina bar, and UI feedback.

## Simulation Mechanics
* Stochasticity: The Lion has a 95% chance of successful movement and a 5% chance of "slipping" into an adjacent cell.
* Stamina Constraint: The Lion begins with 100 stamina points. Every move (including "Stay") consumes 1 point. If stamina reaches 0 before a catch, the Deer wins.
* Environment Validation: A Breadth-First Search (BFS) ensures that the Lion can physically reach the Deer past the 15 randomly placed
*obstacles before the simulation starts.

## Installation & Setup
### 1. Prerequisites
Ensure you have Python 3.13.7 (or a compatible 3.x version) installed.

### 2. Clone the Repository
git clone https://github.com/Jeewan198/Knowledge-Representation-and-Reasoning.git
cd Knowledge-Representation-and-Reasoning

### 3. Install Dependencies
`pip install -r requirements.txt`\

### 4. Asset Requirements
Ensure the following image files are located in the root directory for the GUI to render correctly:
* `lion.png`, `deer.png`, `tree.png`, `rock.png`

### How to Run
Execute the following command to begin the policy calculation and launch the visualizer:

`python main.py`
