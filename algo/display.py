import sys
import numpy as np

sys.path.append("/home/louis/workspace/robinson-shensted")
from algo.algorithms import Involution


def display_involution(inv: Involution):
    for i in range(1, -1, -1):
        print("[", end=" ")
        for element in inv:
            print(element[i], end=" ")
        print("]")


def display_growth_diagram(g_diagram):
    print(np.rot90(g_diagram))


def display_for_python(smth):
    print("[", end="")
    for p in smth[:-1]:
        print("[", end="")
        for e in p[:-1]:
            print(e, end=", ")
        print(p[-1], end="")
        print("], ", end="")
    print("[", end="")
    for e in smth[-1][:-1]:
        print(e, end=", ")
    print(smth[-1][-1], end="")
    print("]]")


def display_for_cpp(smth):
    print(" {", end="")
    for p in smth[:-1]:
        print("{", end="")
        for e in p[:-1]:
            print(e, end=", ")
        print(p[-1], end="")
        print("}, ", end="")
    print("{", end="")
    for e in smth[-1][:-1]:
        print(e, end=", ")
    print(smth[-1][-1], end="")
    print("}}")
