"""
Comparative Table:
    - This script to generate a comparative table between the binary search and the lineal search algorithms.
    - It uses the memory_profiler library to measure the memory usage of the search() method of each algorithm.
    - It uses the time library to measure the time of the search() method of each algorithm.
    - It uses the pandas library to generate the comparative table.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class ComparativeTable:
    def __init__(self):
        self.data = {
            "Algorithm": [],
            "Found": [],
            "Position": [],
            "Comparisons": [],
            "Elapsed Time (ms)": []
        }

    def add_comparative_table(self, algorithm, found, position, comparisons, elapsed_time):
        """
        Generate a comparative table between the binary search and the lineal search algorithms.
        
        Args:
            algorithm: str
                The name of the algorithm.
            found: bool
                True if the number was found, False otherwise.
            position: int
                Position of the number in the array.
            comparsions: int
                Number of comparisons made by the algorithm.
            elapsed_time: float
                Elapsed time in milliseconds.
        """
        self.data["Algorithm"].append(algorithm)
        self.data["Found"].append(found)
        self.data["Position"].append(position)
        self.data["Comparisons"].append(comparisons)
        self.data["Elapsed Time (ms)"].append(elapsed_time)

    def getComparativeTable(self):
        return pd.DataFrame(self.data)
    
    def plot_comparison(self):
        df = self.getComparativeTable()
        
        # Configuración del gráfico
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))

        # Gráfico de Comparaciones
        sns.barplot(x="Algorithm", y="Comparisons", data=df, ax=ax[0], palette="viridis")
        ax[0].set_title("Comparisons by Algorithm")
        ax[0].set_ylabel("Number of Comparisons")

        # Gráfico de Tiempo de Ejecución
        sns.barplot(x="Algorithm", y="Elapsed Time (ms)", data=df, ax=ax[1], palette="coolwarm")
        ax[1].set_title("Elapsed Time by Algorithm")
        ax[1].set_ylabel("Time (ms)")

        plt.tight_layout()
        plt.show()