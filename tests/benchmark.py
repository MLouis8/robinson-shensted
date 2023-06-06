import timeit
import sys

sys.path.append("/Users/louismilhaud/workspace/robinson-shensted")
sys.path.append("/home/louis/workspace/robinson-shensted")

## GLOBAL VAR ##

SETUP_CODE_4 = """
import sys
import json
sys.path.append("/Users/louismilhaud/workspace/robinson-shensted")
sys.path.append("/home/louis/workspace/robinson-shensted")
from algo import (
    Permutation,
    roby_insertion,
    janvier_insertion,
    permutation_to_chains,
    permutation_to_chains_gd
)

data = json.load(open('data/data.json', 'r'))
t4 = data['p4']
p4 = []
for t in t4:
    p4.append(Permutation(t))
"""

SETUP_CODE_8 = """
import sys
import json
sys.path.append("/Users/louismilhaud/workspace/robinson-shensted")
sys.path.append("/home/louis/workspace/robinson-shensted")
from algo import (
    Permutation,
    roby_insertion,
    janvier_insertion,
    permutation_to_chains,
    permutation_to_chains_gd
)

data = json.load(open('data/data.json', 'r'))
t8 = data['p8']
p8 = []
for t in t8:
    p8.append(Permutation(t))
"""

SETUP_CODE_16 = """
import sys
import json
sys.path.append("/Users/louismilhaud/workspace/robinson-shensted")
sys.path.append("/home/louis/workspace/robinson-shensted")
from algo import (
    Permutation,
    roby_insertion,
    janvier_insertion,
    permutation_to_chains,
    permutation_to_chains_gd
)

data = json.load(open('data/data.json', 'r'))
t16 = data['p16']
p16 = []
for t in t16:
    p16.append(Permutation(t))
"""

SETUP_CODE_32 = """
import sys
import json
sys.path.append("/Users/louismilhaud/workspace/robinson-shensted")
sys.path.append("/home/louis/workspace/robinson-shensted")
from algo import (
    Permutation,
    roby_insertion,
    janvier_insertion,
    permutation_to_chains,
    permutation_to_chains_gd
)

data = json.load(open('data/data.json', 'r'))
t32 = data['p32']
p32 = []
for t in t32:
    p32.append(Permutation(t))
"""
SETUP_CODE_64 = """
import sys
import json
sys.path.append("/Users/louismilhaud/workspace/robinson-shensted")
sys.path.append("/home/louis/workspace/robinson-shensted")
from algo import (
    Permutation,
    roby_insertion,
    janvier_insertion,
    permutation_to_chains,
    permutation_to_chains_gd
)

data = json.load(open('data/data.json', 'r'))
t64 = data['p64']
p64 = []
for t in t64:
    p64.append(Permutation(t))
"""

SETUP_CODE_20 = """
import sys
import json
sys.path.append("/Users/louismilhaud/workspace/robinson-shensted")
sys.path.append("/home/louis/workspace/robinson-shensted")
from algo import (
    Permutation,
    roby_insertion,
    janvier_insertion,
    permutation_to_chains,
    permutation_to_chains_gd
)

data = json.load(open('data/data.json', 'r'))
t20 = data['p20']
p20 = []
for t in t20:
    p20.append(Permutation(t))
"""
####


def timer_roby(n):
    TEST_CODE_4 = """
for p in p4:
    _, _ = roby_insertion(p)"""
    TEST_CODE_8 = """
for p in p8:
    _, _ = roby_insertion(p)"""
    TEST_CODE_16 = """
for p in p16:
    _, _ = roby_insertion(p)"""
    TEST_CODE_32 = """
for p in p32:
    _, _ = roby_insertion(p)"""
    TEST_CODE_64 = """
for p in p64:
    _, _ = roby_insertion(p)"""
    TEST_CODE_20 = """
for p in p20:
    _, _ = roby_insertion(p)"""

    return [
        timeit.Timer(setup=SETUP_CODE_4, stmt=TEST_CODE_4).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_8, stmt=TEST_CODE_8).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_16, stmt=TEST_CODE_16).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_32, stmt=TEST_CODE_32).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_64, stmt=TEST_CODE_64).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_20, stmt=TEST_CODE_20).timeit(number=n),
    ]


def timer_janvier(n):
    TEST_CODE_4 = """
for p in p4:
    _, _ = janvier_insertion(p)"""
    TEST_CODE_8 = """
for p in p8:
    _, _ = janvier_insertion(p)"""
    TEST_CODE_16 = """
for p in p16:
    _, _ = janvier_insertion(p)"""
    TEST_CODE_32 = """
for p in p32:
    _, _ = janvier_insertion(p)"""
    TEST_CODE_64 = """
for p in p64:
    _, _ = janvier_insertion(p)"""
    TEST_CODE_20 = """
for p in p20:
    _, _ = janvier_insertion(p)"""

    return [
        timeit.Timer(setup=SETUP_CODE_4, stmt=TEST_CODE_4).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_8, stmt=TEST_CODE_8).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_16, stmt=TEST_CODE_16).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_32, stmt=TEST_CODE_32).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_64, stmt=TEST_CODE_64).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_20, stmt=TEST_CODE_20).timeit(number=n),
    ]


def timer_permu2chains(n):
    TEST_CODE_4 = """
for p in p4:
    _, _ = permutation_to_chains(p)"""
    TEST_CODE_8 = """
for p in p8:
    _, _ = permutation_to_chains(p)"""
    TEST_CODE_16 = """
for p in p16:
    _, _ = permutation_to_chains(p)"""
    TEST_CODE_32 = """
for p in p32:
    _, _ = permutation_to_chains(p)"""
    TEST_CODE_64 = """
for p in p64:
    _, _ = permutation_to_chains(p)"""
    TEST_CODE_20 = """
for p in p20:
    _, _ = permutation_to_chains(p)"""

    return [
        timeit.Timer(setup=SETUP_CODE_4, stmt=TEST_CODE_4).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_8, stmt=TEST_CODE_8).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_16, stmt=TEST_CODE_16).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_32, stmt=TEST_CODE_32).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_64, stmt=TEST_CODE_64).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_20, stmt=TEST_CODE_20).timeit(number=n),
    ]


def timer_permu2chains_gd(n):
    TEST_CODE_4 = """
for p in p4:
    _, _ = permutation_to_chains_gd(p)"""
    TEST_CODE_8 = """
for p in p8:
    _, _ = permutation_to_chains_gd(p)"""
    TEST_CODE_16 = """
for p in p16:
    _, _ = permutation_to_chains_gd(p)"""
    TEST_CODE_32 = """
for p in p32:
    _, _ = permutation_to_chains_gd(p)"""
    TEST_CODE_64 = """
for p in p64:
    _, _ = permutation_to_chains_gd(p)"""
    TEST_CODE_20 = """
for p in p20:
    _, _ = permutation_to_chains_gd(p)"""

    return [
        timeit.Timer(setup=SETUP_CODE_4, stmt=TEST_CODE_4).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_8, stmt=TEST_CODE_8).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_16, stmt=TEST_CODE_16).timeit(number=n),
        # timeit.Timer(setup=SETUP_CODE_32, stmt=TEST_CODE_32).timeit(number=n), python limits reached
        # timeit.Timer(setup=SETUP_CODE_64, stmt=TEST_CODE_64).timeit(number=n),
        timeit.Timer(setup=SETUP_CODE_20, stmt=TEST_CODE_20).timeit(number=n),
    ]


def time_roby_insertion(n=1):
    tab = timer_roby(n)
    print("Roby Insertion algorithm:")
    print(f"50 4-permutations: {tab[0]:2.5e}, {n} time")
    print(f"50 8-permutations: {tab[1]:2.5e}, {n} time")
    print(f"50 16-permutations: {tab[2]:2.5e}, {n} time")
    print(f"50 32-permutations: {tab[3]:2.5e}, {n} time")
    print(f"50 64-permutations: {tab[4]:2.5e}, {n} time")
    print(f"1000 20-permutations: {tab[5]:2.5e}, {n} time")


def time_janvier_insertion(n=1):
    tab = timer_janvier(n)
    print("Janvier Insertion algorithm:")
    print(f"50 4-permutations: {tab[0]:2.5e}, {n} time")
    print(f"50 8-permutations: {tab[1]:2.5e}, {n} time")
    print(f"50 16-permutations: {tab[2]:2.5e}, {n} time")
    print(f"50 32-permutations: {tab[3]:2.5e}, {n} time")
    print(f"50 64-permutations: {tab[4]:2.5e}, {n} time")
    print(f"1000 20-permutations: {tab[5]:2.5e}, {n} time")


def time_permutation_to_chains(n=1):
    tab = timer_permu2chains(n)
    print("Permutation to YF chains algorithm:")
    print(f"50 4-permutations: {tab[0]:2.5e}, {n} time")
    print(f"50 8-permutations: {tab[1]:2.5e}, {n} time")
    print(f"50 16-permutations: {tab[2]:2.5e}, {n} time")
    print(f"50 32-permutations: {tab[3]:2.5e}, {n} time")
    print(f"50 64-permutations: {tab[4]:2.5e}, {n} time")
    print(f"1000 20-permutations: {tab[5]:2.5e}, {n} time")


def compare_permutation_to_chains(n=1):
    tab1 = timer_permu2chains(n)
    tab2 = timer_permu2chains_gd(n)
    print("Comparison of the two algorithms:\n")
    print("The first one creates the growth diagram and extract from it the chains:")
    print(f"    50 4-permutations: {tab2[0]:2.5e}, {n} time")
    print(f"    50 8-permutations: {tab2[1]:2.5e}, {n} time")
    print(f"    50 16-permutations: {tab2[2]:2.5e}, {n} time")
    # print(f"    50 32-permutations: {tab2[3]:2.5e}, {n} time") python limits reached
    # print(f"    50 64-permutations: {tab2[4]:2.5e}, {n} time")
    print(f"    1000 20-permutations: {tab2[3]:2.5e}, {n} time\n")
    print("The second one directly computes the chains from the permutation")
    print(f"    50 4-permutations: {tab1[0]:2.5e}, {n} time")
    print(f"    50 8-permutations: {tab1[1]:2.5e}, {n} time")
    print(f"    50 16-permutations: {tab1[2]:2.5e}, {n} time")
    # print(f"    50 32-permutations: {tab1[3]:2.5e}, {n} time")
    # print(f"    50 64-permutations: {tab1[4]:2.5e}, {n} time")
    print(f"    1000 20-permutations: {tab1[5]:2.5e}, {n} time\n")
