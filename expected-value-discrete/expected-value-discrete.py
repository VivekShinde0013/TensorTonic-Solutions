import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x=np.array(x)
    p=np.array(p)

    if x.shape != p.shape:
        raise ValueError("The number of values (x) and probabilities (p) must match.")
    if np.any(p < 0) or np.any(p > 1):
        raise ValueError("Individual probabilities must be between 0 and 1 inclusive.")

    if not np.isclose(np.sum(p), 1.0):
        raise ValueError("The sum of all probabilities must equal 1.")
    return np.sum(x*p)
    pass
