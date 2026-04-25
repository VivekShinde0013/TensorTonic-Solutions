import numpy as np
import torch
def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    seq_tensors=[torch.tensor(s) if not isinstance(s,torch.Tensor) else s for s in seqs]
    if max_len is None:
        max_len = max(len(s) for s in seq_tensors)
        
    batch_size=len(seq_tensors)

    padded_tensor=torch.full((batch_size, max_len), pad_value, dtype=seq_tensors[0].dtype)

    for i, seq in enumerate(seq_tensors):
        length=min(len(seq), max_len)
        padded_tensor[i, :length]=seq[:length]

    return padded_tensor

data=[[1,2,3],[4,5],[6]]

print(pad_sequences(data))
