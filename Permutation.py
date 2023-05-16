class Permutation:
    def __init__(self, t):
        #self.check_init(t)
        m = min(t)
        self._permu_dict = {}
        for idx, elem in enumerate(t):
            self._permu_dict[idx+m] = elem

    def __getitem__(self, key):
        return self._permu_dict[key]

    @property
    def _get_keys(self):
        return self._permu_dict.keys()