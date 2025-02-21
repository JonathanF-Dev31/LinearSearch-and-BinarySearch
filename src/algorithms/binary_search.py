"""
Class BinarySearch:

    This class is responsible for searching a number using the binary search algorithm in an array of 150 elements.

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

class BinarySearch(AlgorithmSearch):
    def __init__(self, array):
        super().__init__(array)
        self.algorithm = "Binary Search"

    @profile # Decorator to measure the search() method
    def search(self, number):
        comparisons = 0
        start_time = time.perf_counter() # Start time to measure the search() method
        found = False
        min = 1
        max = len(self.array) -1
        target = number
        guess = 0
        while min <= max:
            comparisons += 1
            guess = (max + min) // 2
            if target == self.array[guess]:
                found = True
                break
            elif target > self.array[guess]:
                min = guess +1
            else:
                max = guess -1
    
        end_time = time.perf_counter() # End time to measure the search() method

        elapsed_time = (end_time - start_time) * 1000 # Elapsed time in milliseconds

        if found:
            return self.algorithm, True, guess, comparisons, elapsed_time
        else:
            return self.algorithm, False, -1, comparisons, elapsed_time



