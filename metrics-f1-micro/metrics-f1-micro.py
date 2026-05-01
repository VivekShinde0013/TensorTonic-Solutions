from sklearn.metrics import f1_score
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    return f1_score(y_true,y_pred,average='micro')
    pass