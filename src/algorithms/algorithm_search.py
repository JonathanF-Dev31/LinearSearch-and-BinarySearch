"""
Class AlgorithmSearch:

    This a interface class that defines the methods that must be implemented 
    by the classes that will use the search algorithm as class LinealSearch and class BinarySearch.
"""

from abc import ABC, abstractmethod

class AlgorithmSearch(ABC):
    def __init__(self, array):
        self.array = sorted(array)
        self.algorithm = None
        
    def getArray(self):
        return self.array
    
    @abstractmethod     
    def search(self, number):
        pass

