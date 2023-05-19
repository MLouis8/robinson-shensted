from Permutation import Permutation
from RS_Fomin_permutations import roby_insertion, evacuation, permu_to_growth_diagram, paths_to_growth_diagram, permu_to_y_f_path, compute_path_table
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
p1, q1 = [[7, 6, 5, 2], [3, 4, None, 1]], [[2, 6, 5, 1], [3, 7, None, 4]]

assert roby_insertion(perm1) == (p1, q1)

p1_tilda = [[3, 5, 7, 1], [4, 6, None, 2]]

assert evacuation(p1) == p1_tilda

#print(permu_to_growth_diagram(perm1))

p1, p2 = permu_to_y_f_path(perm1)
#print(paths_to_growth_diagram(p1, p2))

print(compute_path_table(p1))