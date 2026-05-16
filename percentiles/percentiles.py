import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    return np.atleast_1d(np.percentile(x,q))
    pass