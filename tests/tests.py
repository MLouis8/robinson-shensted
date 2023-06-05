import sys
import numpy as np

sys.path.append("/home/louis/workspace/robinson-shensted")
from algo import (
    Permutation,
    robinson_schensted,
    roby_insertion,
    evacuation,
    permutation_to_chains_gd,
    chain_to_path_tableau,
    standard_YFT_to_chain,
    random_permutations
)

testV1 = [3, 8, 4, 1, 2]
testC1 = [[1, 2], [3, 4], [8]]
testV2 = [3, 2]
testC2 = [[2], [3]]
testV3 = "acdbaedbc"
testC3 = [["a", "a", "b", "c"], ["b", "d", "d"], ["c", "e"]]

# assert robinson_schensted(testV1) == testC1
# assert robinson_schensted(testV2) == testC2
# assert robinson_schensted(testV3) == testC3

perm1 = Permutation([2, 7, 1, 5, 6, 4, 3])
# p1, q1 = ([7, 6, 5, 2], [3, 4, 0, 1]), ([2, 6, 5, 1], [3, 7, 0, 4])

# assert roby_insertion(perm1) == (p1, q1)

# p1_tilda = ([3, 5, 7, 1], [4, 6, 0, 2])

# assert evacuation(p1) == p1_tilda

# # print(permutation_to_growth_diagram(perm1))

# p1, p2 = permutation_to_chains_gd(perm1)
# # print(chains_to_growth_diagram(p1, p2))
# print(p1)
# print(chain_to_path_tableau(p1))
# print(chain_to_path_tableau([0, 1, 11, 21, 22, 212, 222, 2122, 2222]))
p = Permutation([3, 1, 4, 2])
# print(permutation_to_chains(p))

# perm2 = Permutation([4, 3, 1, 2])
# print(permutation_to_growth_diagram(perm2))

# print(chain_to_standard_YFT([0, 1, 2, 12, 22, 221, 2211, 21211]))

# print(standard_YFT_to_chain(([3, 6, 1, 4, 2], [7, 0, 5, 0, 0])))

# print(chain_to_standard_YFT([0, 1, 2, 21]))
# print(chain_to_standard_YFT([0, 1, 11, 21]))
# print(chain_to_standard_YFT([0, 1, 11, 111]))

# print(standard_YFT_to_chain(chain_to_standard_YFT([0, 1, 2, 21])))
# print(standard_YFT_to_chain(chain_to_standard_YFT([0, 1, 11, 21])))
# print(standard_YFT_to_chain(([2, 1], [3, 0])))

# print(chain_to_standard_YFT([0, 1, 11, 21, 22, 212, 2112, 2212]))
# print(chain_to_standard_YFT([0, 1, 2, 12, 22, 212, 222, 2212]))

# perm3 = Permutation([5, 3, 4, 1, 2])
# inv1, inv2 = roby_insertion(perm3)

# perm4 = Permutation([5, 2, 1, 3, 4])
# print(roby_insertion(perm4))

p3 = Permutation([7, 3, 1, 5, 8, 4, 6, 2])
# print(roby_insertion(p3))

# print(evacuation(([[7, 3], [6, 4], [5, 0], [2, 1]])))
print(standard_YFT_to_chain(([3, 6, 1, 4, 2], [7, 0, 5, 0, 0])))
print(standard_YFT_to_chain(([2, 6, 4, 1], [8, 7, 5, 3])))
print(standard_YFT_to_chain(([5, 1, 4, 2], [8, 7, 6, 3])))

print(random_permutations(23, 456))