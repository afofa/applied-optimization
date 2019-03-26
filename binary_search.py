import numpy as np
from typing import Callable, Generator, Tuple

def binary_search(  f:Callable, 
                    low:float=-10.0, 
                    high:float=10.0, 
                    num_of_points:int=7, 
                    num_of_iterations:int=10
                ):
    def generate_and_evaluate(f:Callable, low:float, high:float, num_of_points:int) -> Tuple[np.ndarray, Generator[float, None, None]]:
        xs = np.linspace(low, high, num_of_points)
        ys = map(f, xs)

        return xs, ys

    def get_low_and_high(xs:np.ndarray, ys:Generator[float, None, None]) -> Tuple[float, float, float, float]:
        # smallest and 2nd smallest values and corresponding indices
        min1, min2 = np.inf, np.inf
        ind1, ind2 = 0, 0
        
        for i, y in enumerate(ys):
            if y < min1:
                min1, min2 = y, min1
                ind1, ind2 = i, ind1
            elif y < min2:
                min2 = y
                ind2 = i

        return xs[ind1], xs[ind2], min1, min2

    mins = np.zeros((num_of_iterations))

    for i in range(num_of_iterations):
        print(f"Iteration {i+1}:")
        xs, ys = generate_and_evaluate(f, low, high, num_of_points)
        low, high, min1, min2 = get_low_and_high(xs, ys)
        print(f"Low: {low}, High: {high}")
        print(f"min1: {min1}, min2: {min2}")
        mins[i] = min1

    return mins
