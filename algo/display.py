import sys
import numpy as np

sys.path.append("/home/louis/workspace/robinson-shensted")
from algo.algorithms import Involution

def display_involution(inv: Involution):
    for i in range(1, -1, -1):
        print('[', end=' ')
        for element in inv:
            print(element[i], end=' ')
        print(']')

def display_growth_diagram(g_diagram):
    print(np.rot90(g_diagram))