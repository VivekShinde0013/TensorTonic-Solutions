import numpy as np
import math
def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    if not x or not y:
        raise ValueError("Input vectors must not be empty")\
    
    if len(x) != len(y):
        raise ValueError("Input vectors must have the same length")
            
    return math.sqrt(sum((a-b)**2 for a, b in zip(x,y)))
    