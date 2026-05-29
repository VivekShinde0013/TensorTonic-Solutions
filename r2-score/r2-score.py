import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    mean_y = sum(y_true) / len(y_true)

    ss_total = sum((y - mean_y) ** 2 for y in y_true)
    ss_residual = sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred))

    if ss_total == 0:
        return 1.0 if ss_residual == 0 else 0.0

    return 1 - (ss_residual / ss_total)