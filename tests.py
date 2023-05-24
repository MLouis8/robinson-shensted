from Permutation import Permutation
from algorithms import *
from RS_suites_extraites import robinson_schensted
import numpy as np

testV1 = [3, 8, 4, 1, 2]
testC1 = [[1, 2], [3, 4], [8]]
testV2 = [3, 2]
testC2 = [[2], [3]]
testV3 = 'acdbaedbc'
testC3 = [['a', 'a', 'b', 'c'], ['b', 'd', 'd'], ['c', 'e']]

assert robinson_schensted(testV1) == testC1
assert robinson_schensted(testV2) == testC2
assert robinson_schensted(testV3) == testC3

perm1 = Permutation([2, 7, 1, 5, 6, 4, 3])
p1, q1 = ([7, 6, 5, 2], [3, 4, 0, 1]), ([2, 6, 5, 1], [3, 7, 0, 4])

assert roby_insertion(perm1) == (p1, q1)

p1_tilda = ([3, 5, 7, 1], [4, 6, 0, 2])

assert evacuation(p1) == p1_tilda

#print(permu_to_growth_diagram(perm1))

p1, p2 = permutation_to_chains_gd(perm1)
#print(chains_to_growth_diagram(p1, p2))
#print(compute_path_table(p1))

p = Permutation([3, 1, 4, 2])
#print(permu_to_chains(p))

perm2 = Permutation([4, 3, 1, 2])
# print(permu_to_growth_diagram(perm2))