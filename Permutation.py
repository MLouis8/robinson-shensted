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
    def __getitem__(self, key):
        return self._permu_dict[key]

    def _display_matrix():
        print(self._permu_matrix)

    @property
    def _get_keys(self):
        return self._permu_dict.keys()