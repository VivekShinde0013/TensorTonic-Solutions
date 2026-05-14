import numpy as np
import math

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    n=len(x)
    mean=sum(x)/n
    sum_s=sum((item-mean)**2 for item in x)
    sample=sum_s/(n-1)
    sample_d=math.sqrt(sample)
    return sample, sample_d
    pass