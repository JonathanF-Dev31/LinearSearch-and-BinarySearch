"""
Task 2: Searcher

It searches for a number in an array of 150 numbers and determines if it was found or not.

"""
import random
from algorithms.lineal_search import LinealSearch
from algorithms.binary_search import BinarySearch
from utils.comparative_table import ComparativeTable

def main():
    random.seed(42)
    array = random.sample(range(0, 1001), 150)
    print(sorted(array))
    print("")
    
    search_value = random.choice(array)
    print(f"Searching for the number: {search_value}")
    print("")

    searcher_one_by_one = LinealSearch(array)
    searcher_one_by_one.search(search_value)

    searcher_binary = BinarySearch(array)
    searcher_binary.search(search_value)


    table = ComparativeTable()

    table.add_comparative_table(*searcher_one_by_one.search(search_value))

    table.add_comparative_table(*searcher_binary.search(search_value))

    table.plot_comparison()

if __name__ == "__main__":
    main()
