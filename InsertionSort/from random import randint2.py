from random import randint
from timeit import repeat
import time


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    start = time.time()

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    end = time.time()

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
    print(f"Algorithm: {algorithm}. Execution time: {end - start}")

 

array = [9,8,8,7,7,2,9,3,4,1]


def insertion_sort(array):
    n = len(array)

    for i in range(1, n):

        if array[i]<array[i-1]:
            array[i-1], array[i] = array[i], array[i-1]

        for j in range(i-1, 0, -1):

            if array[j]<array[j-1]: 
                array[j-1], array[j] = array[j], array[j-1]


insertion_sort(array)
print(array)