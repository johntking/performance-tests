import numpy as np
from multiprocessing import Pool



def mp_np(N):

    def inner():
        X = np.random.randn(N**3)
        yield 'randn'
        X = X.reshape(N, N, N)
        yield 'reshape'
        m1 = X.min(axis = 2).max(axis = 1).min()
        yield 'dim-m/m'
        X = X / m1
        yield 'divide'
        X = X ** 3
        yield 'power'
        X = X[X > 1]
        yield 'boolmask'
        X = np.sort(X, axis = 0)
        yield 'sort'
        m2 = X[int(len(X) / 2)]
        yield 'select'

    return inner








