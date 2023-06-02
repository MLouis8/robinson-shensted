import sys

sys.path.append("/home/louis/workspace/robinson-shensted")
from algo import Permutation, janvier_insertion, check_standard_yf_tableau

p1 = Permutation([2, 3, 1])
p2 = Permutation([1, 3, 2])
p3 = Permutation([5, 3, 4, 1, 2])
p4 = Permutation([5, 2, 1, 3, 4])

std_tabs = janvier_insertion(p1)
check_standard_yf_tableau(std_tabs[0])
check_standard_yf_tableau(std_tabs[1])
std_tabs = janvier_insertion(p2)
check_standard_yf_tableau(std_tabs[0])
check_standard_yf_tableau(std_tabs[1])
std_tabs = janvier_insertion(p3)
check_standard_yf_tableau(std_tabs[0])
check_standard_yf_tableau(std_tabs[1])
std_tabs = janvier_insertion(p4)
check_standard_yf_tableau(std_tabs[0])
check_standard_yf_tableau(std_tabs[1])
