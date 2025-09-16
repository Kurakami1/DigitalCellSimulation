"""
multicell_sim_viz.py
Digital simulation of multicellular system with visualization
"""

from cell_simulation_viz import Cell
import matplotlib.pyplot as plt
import random

class Tissue:
    def __init__(self, name="Tissue-1", cell_count=5):
        self.name = name
        self.cells = [Cell(name=f"{self.name}-Cell{i+1}") for i in range(cell_count)]

    def simulate_step(self):
        new_cells = []
        for cell in self.cells:
            cell.simulate_step()
            daughter = cell.divide()
            if daughter:
                new_cells.append(daughter)
        self.cells.extend(new_cells)

class Organism:
    def __init__(self):
        self.tissues = [
            Tissue("Epithelial", 5),
            Tissue("Muscle", 5),
            Tissue("Nerve", 3)
        ]

    def simulate_step(self):
        for tissue in self.tissues:
            tissue.simulate_step()

    def average_ATP(self):
        all_cells = [c for t in self.tissues for c in t.cells]
        return sum(c.ATP for c in all_cells)/len(all_cells)

    def total_cells(self):
        return sum(len(t.cells) for t in self.tissues)

# ---------------- Simulation with visualization ----------------
if __name__ == "__main__":
    organism = Organism()
    steps = 20
    ATP_history = []
    cell_history = []

    for step in range(steps):
        organism.simulate_step()
        ATP_history.append(organism.average_ATP())
        cell_history.append(organism.total_cells())

    # Plot results
    plt.figure(figsize=(10,5))
    plt.plot(ATP_history, label="Average ATP")
    plt.plot(cell_history, label="Total Cell Count")
    plt.xlabel("Simulation Step")
    plt.ylabel("Values")
    plt.title("Multicellular Organism Simulation")
    plt.legend()
    plt.show()
