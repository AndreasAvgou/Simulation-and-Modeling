# 🖥️ Simulation & Modeling

This project provides a complete set of Python simulations inspired by Simulation & Modeling course material.
It includes models of malware spreading, immunity dynamics, information transmission, earthquake (sandpile) systems,
and M/M/1 queueing behavior.


## Required Packages

```bash
pip install matplotlib numpy
```
## Running the Project

Run any simulation script:
```bash
python malware_no_immunity.py
python malware_with_immunity.py
python information_spread.py
python earthquake_simulation.py
python mm1_queue.py
```
Each script will automatically show a plot of the simulation results.

## Description of Each Component

### 1. Malware Spread (No Immunity)
Basic SI-model simulation where infected nodes infect random healthy nodes.

### 2. Malware Spread With Immunity
SIR-like model where infected nodes eventually become immune.

### 3. Information Spread
Stochastic model where only one random node attempts to transmit information at each step.

### 4. Earthquake Simulation (Sandpile / Avalanche)
Self-organized criticality model producing avalanches of various sizes.

### 5. M/M/1 Queue Simulation
Classic queue simulation showing stability when λ < μ and divergence when λ > μ.

## Tips

- You can adjust simulation duration, population size, etc.
- Matplotlib plots will open automatically.
- NumPy is only required for the earthquake model.

