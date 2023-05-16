from Permutation import Permutation
from RS_Fomin_permutations import roby_insertion
from RS_suites_extraites import robinson_schensted

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