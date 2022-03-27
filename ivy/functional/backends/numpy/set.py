# global
import numpy as np
from typing import Tuple
from collections import namedtuple
from packaging import version


def unique_inverse(x: np.ndarray) \
        -> Tuple[np.ndarray, np.ndarray]:
    out = namedtuple('unique_inverse', ['values', 'inverse_indices'])
    values, inverse_indices = np.unique(x, return_inverse=True)
    if x.shape == ():
        inverse_indices = inverse_indices.reshape(())
    return out(values, inverse_indices)


def unique_values(x: np.ndarray)\
        -> np.ndarray:
    nan_count = np.count_nonzero(np.isnan(x))
    if (version.parse(np.__version__) >= version.parse('1.21.0') and nan_count > 1):
        unique = np.append(np.unique(x.flatten()), np.full(nan_count - 1, np.nan)).astype(x.dtype)
    else:
        unique = np.unique(x.flatten()).astype(x.dtype)
    return unique