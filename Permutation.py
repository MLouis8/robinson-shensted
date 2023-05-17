import numpy as np

class Permutation:
    def __init__(self, t):
        #self.check_init(t)
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
        return self._permu_dict.keys()

    @property
    def matrix(self):
        return self._permu_matrix