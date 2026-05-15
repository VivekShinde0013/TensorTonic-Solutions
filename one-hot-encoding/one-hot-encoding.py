import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    y=np.array(y,dtype='int')
    if not num_classes:
        num_classes=np.max(y)+1
    return np.eye(num_classes)[y]
    pass