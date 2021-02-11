import os
import numpy as np
from multiprocessing import Pool


def randn_mul_save_load_delete(path, n):
    a, b = np.random.randn(2 * n).reshape(2, n)
    np.save(path, a * b)
    _ = np.load(path)
    os.remove(path)


PATH_HEAD = 'temp-testing'

def mp_np(arr_size, max_cores, iterable_size):

    def inner():
        os.makedirs(PATH_HEAD, exist_ok = True)
        iterable = [(f'{PATH_HEAD}/{i}.npy', arr_size) for i in range(iterable_size)]
        for n in range(1 + max_cores):
            if n == 0:
                _ = [randn_mul_save_load_delete(*args) for args in iterable]
                yield 'no-mp'
            else:
                with Pool(processes = n) as pool:
                    _ = pool.starmap(randn_mul_save_load_delete, iterable)
                yield f'cores={n}'

    return inner








