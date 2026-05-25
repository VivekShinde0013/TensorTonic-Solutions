import numpy as np
from collections import Counter
def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    majority=Counter(y_train).most_common(1)[0][0]
    return np.array([majority] * len(X_test))
    pass