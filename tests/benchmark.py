import timeit
import sys

sys.path.append("/home/louis/workspace/robinson-shensted")


def time_roby_insertion():
    SETUP_CODE = """
import sys
sys.path.append("/home/louis/workspace/robinson-shensted")
from algo import Permutation, roby_insertion
p = Permutation([5, 2, 6, 7, 3, 4, 8, 1])"""
    TEST_CODE = """
_, _ = roby_insertion(p)"""

    return timeit.Timer(setup=SETUP_CODE, stmt=TEST_CODE).timeit(number=1)


print(time_roby_insertion())
