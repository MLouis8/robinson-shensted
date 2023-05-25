import numpy as np

class Permutation:
    def __init__(self, t):
        def check_init(t):
            mem = []
            for i in t:
                if not isinstance(i, int):
                    raise TypeError("Values must be integers.")
                if i > len(t) or i < 1:
                    raise ValueError("Permutation not valid. Values must be within [1, len(array)].")
                if i in mem:
                    raise ValueError("Permutation not valid. Values must appear once.")
                mem.append(i)
        check_init(t)
        m = min(t)
        self._permu_dict = {}
        self._permu_matrix = np.zeros((len(t), len(t)))
        for idx, elem in enumerate(t):
            self._permu_dict[idx+m] = elem
            self._permu_matrix[idx, elem-m] = 1
        self._permu_matrix = self._permu_matrix.transpose()

    def __getitem__(self, key):
        return self._permu_dict[key]

    def _display_matrix(self):
        for i in range(-1, -self._permu_matrix.shape[0]-1, -1):
            print(self._permu_matrix[i])

    @property
    def size(self):
        return len(self._permu_dict.keys())

    @property
    def keys(self):
        return list(self._permu_dict.keys())
    
    @property
    def table(self):
        return list(self._permu_dict.values())

    @property
    def matrix(self):
        return self._permu_matrix