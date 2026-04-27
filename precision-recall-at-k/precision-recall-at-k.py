def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    tkc=recommended[:k]
    rs=set(relevant)
    nrk=sum(1 for item in tkc if item in rs)
    precision=nrk/k if k>0 else 0.0
    recall=nrk/len(relevant) if len(relevant)>0 else 0.0

    return [precision, recall]