"""
Class LinealSearch: 

This class is responsible for searching a number one by one in an array of 150 elements.

Args:
    number: int
        The number to search for in the array.
Returns:
    bool: Result of the search.
        True if the number was found, False otherwise.
    int: Position of the number in the array.
        -1 if the number was not found.

"""

from memory_profiler import profile
import time
from algorithms.algorithm_search import AlgorithmSearch

class LinealSearch(AlgorithmSearch):
    def __init__(self, array):
        super().__init__(array)
        self.algorithm = "Lineal Search"
    
    @profile # Decorator to measure the search() method        
    def search(self, number):
        comparisons = 0
        start_time = time.perf_counter() # Start time to measure the search() method
        
        for i in range(len(self.array)):
            comparisons += 1
            if self.array[i] == number:
                found = True
                break
            else:
                found = False
        
        end_time = time.perf_counter() # End time to measure the search() method

        elapsed_time = (end_time - start_time) * 1000 # Elapsed time in milliseconds
       
        if found:
            position = self.array.index(number)       
            return self.algorithm, True, position, comparisons, elapsed_time
        else:
            return self.algorithm, False, -1, comparisons, elapsed_time