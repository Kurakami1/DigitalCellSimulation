"""
cell_simulation_viz.py
Digital simulation of a single eukaryotic cell with visualization
"""

import random
import matplotlib.pyplot as plt

class Cell:
    def __init__(self, name="Cell-1"):
        self.name = name
        self.DNA_integrity = 0.999997
        self.ATP = 1.0
        self.protein_synthesis_rate = 1.0
        self.age = 0
        self.ready_to_divide = False

    def metabolize(self):
        production = random.uniform(0.9, 1.1)
        consumption = random.uniform(0.8, 1.0)
        self.ATP += production - consumption
        if self.ATP < 0:
            self.ATP = 0

    def synthesize_proteins(self):
        error_rate = 0.0001
        if random.random() < error_rate:
            self.DNA_integrity -= error_rate
        self.protein_synthesis_rate = max(0, self.protein_synthesis_rate)

    def check_division(self):
        if self.ATP > 1.0 and self.DNA_integrity > 0.999:
            self.ready_to_divide = True

    def divide(self):
        if self.ready_to_divide:
            daughter = Cell(name=self.name + "-D")
            daughter.DNA_integrity = self.DNA_integrity
            daughter.ATP = self.ATP / 2
            self.ATP /= 2
            self.ready_to_divide = False
            return daughter
        return None

    def simulate_step(self):
        self.metabolize()
        self.synthesize_proteins()
        self.check_division()
        self.age += 1

# ---------------- Simulation with visualization ----------------
if __name__ == "__main__":
    cell = Cell()
    steps = 20
    ATP_history = []
    DNA_history = []
    cell_count = [1]

    cells = [cell]

    for step in range(steps):
        new_cells = []
        for c in cells:
            c.simulate_step()
            daughter = c.divide()
            if daughter:
                new_cells.append(daughter)
        cells.extend(new_cells)
        cell_count.append(len(cells))
        ATP_history.append(sum(c.ATP for c in cells)/len(cells))
        DNA_history.append(sum(c.DNA_integrity for c in cells)/len(cells))

    # Plot results
    plt.figure(figsize=(10,5))
    plt.plot(ATP_history, label="Average ATP")
    plt.plot(DNA_history, label="Average DNA Integrity")
    plt.plot(cell_count[1:], label="Cell Count")
    plt.xlabel("Simulation Step")
    plt.ylabel("Values")
    plt.title("Single Cell Simulation with Division")
    plt.legend()
    plt.show()
