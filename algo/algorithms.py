import sys
from typing import List, Tuple
import numpy as np

sys.path.append("/home/louis/workspace/robinson-shensted")
from algo.Permutation import Permutation

Involution = List[List[int]]
Tableau = Tuple[List[int], List[int]]
STableau = Tuple[List[int], List[int]]
Chain = List[int]


def roby_insertion(p: Permutation) -> Tuple[Involution, Involution]:
    """Roby's Insertion algorithm.
    Relation: Permutation p -> Involutions (inv1, inv2)
    0 stands for empty.
    >>> roby_insertion(Permutation([2, 7, 1, 5, 6, 4, 3]))
    ([[7, 3], [6, 4], [5, 0], [2, 1]], [[2, 3], [6, 7], [5, 0], [1, 4]])
    """

    def insert(
        element: int, key: int, inv1: Involution, inv2: Involution, id_c: int
    ) -> None:
        if element < inv1[id_c][0]:
            if inv1[id_c][1] == 0:
                inv1[id_c][1] = element
                inv2[id_c][1] = key
            else:
                temp = inv1[id_c][1]
                inv1[id_c][1] = element
                if len(inv1) == id_c + 1:
                    inv1.append([temp, 0])
                    inv2.append([key, 0])
                else:
                    insert(temp, key, inv1, inv2, id_c + 1)
        else:
            inv1.insert(id_c, [element, 0])
            inv2.insert(id_c, [key, 0])

    inv1: Involution = [[p[1], 0]]
    inv2: Involution = [[1, 0]]
    for k in p.keys[1:]:
        insert(p[k], k, inv1, inv2, 0)
    return inv1, inv2


def evacuation(inv: Involution) -> Tableau:
    """Killpatrick's evacuation algorithm.
    Relation: Involution inv -> path tableau

    Attention on suppose ici que p[0][0] contienne le nombre d'elements de p
    0 stands for empty

    >>> evacuation(([[7, 3], [6, 4], [5, 0], [2, 1]]))
    ([3, 5, 7, 1], [4, 6, 0, 2])
    """

    def find_evac_point(p: Involution) -> Tuple[int, int, int]:
        def compare_neighbors(i: int, j: int, inv: Involution) -> Tuple[int, int]:
            if inv[i][j + 1] == 0:  # ligne dessus vide
                inv[i][j] = 0
                return j, i
            if (
                len(inv) == i + 1 or inv[i + 1][j] == 0 or inv[i][j + 1] > inv[i + 1][j]
            ):  # fin de la liste ou voisin droite vide ou voisin dessus > voisin droite
                inv[i][j] = inv[i][j + 1]
                inv[i][j + 1] = 0
                return j + 1, i
            else:  # voisin dessus <= voisin droite
                inv[i][j] = inv[i + 1][j]
                inv[i + 1][j] = 0
                return compare_neighbors(i + 1, j, inv)

        i = 0
        while inv[i][0] == 0:
            i += 1
        tmp = inv[i][0]
        x, y = compare_neighbors(i, 0, inv)
        return tmp, x, y

    path_tableau: Tableau = ([0] * len(inv), [0] * len(inv))
    for i in range(inv[0][0]):
        e, x, y = find_evac_point(inv)
        path_tableau[x][y] = e
    return path_tableau


def chain_to_path_tableau(p: Chain) -> Tableau:
    """Computes path tableau
    Relation: Young-Fibonacci lattice chain p -> path tableau tab

    >>> chain_to_path_tableau([0, 1, 2, 12, 22, 212, 222, 2212])
    ([3, 5, 7, 1], [4, 6, 0, 2])
    """

    def path_tableau_rules(
        a: List[int], b: List[int], k: int, l: int, flag: bool
    ) -> Tuple[int, int, List[int]]:
        match a[k]:
            case 1:
                if flag:
                    a[k] = 0
                    return 0, k, a
                if len(b) == l:
                    return path_tableau_rules(a, b, 0, 0, True)
                elif b[l] == 2 or b[l] == 0:  # ajout d'un 1
                    a[k] = 0
                    return 0, k, a
                return path_tableau_rules(a, b, k + 1, l + 1, flag)
            case 2:
                if b[l] == 1 or b[l] == 0:  # transformation d'un 1
                    a[k] = 1
                    return 1, k, a
                else:
                    return path_tableau_rules(a, b, k + 1, l + 1, flag)
            case _:
                return path_tableau_rules(a, b, k + 1, l, flag)

    act = [int(i) for i in str(p[-1])]
    tab: Tableau = ([0] * len(act), [0] * len(act))
    s = sum(act)
    for k in range(-2, -len(p) - 1, -1):
        i, j, act = path_tableau_rules(act, [int(h) for h in str(p[k])], 0, 0, False)
        tab[i][j] = s
        s -= 1
    return tab


def permutation_to_chains(perm: Permutation) -> Tuple[Chain, Chain]:
    """Returns pair of chains in the Young-Fibonacci lattice from a permutation, optimized version.
    Relation: Permutation perm -> Young-Fibonacci lattice chains (p, q)

    >>> permutation_to_chains(Permutation([3, 1, 4, 2]))
    ([0, 1, 11, 21, 22], [0, 1, 2, 12, 22])

    >>> permutation_to_chains(Permutation([2, 7, 1, 5, 6, 4, 3]))
    ([0, 1, 2, 12, 22, 212, 222, 2212], [0, 1, 11, 21, 22, 212, 2112, 2212])
    """

    def compute_fibo_node(dg: np.ndarray) -> int:
        def list_to_int(l: List[int]) -> int:
            res = 0
            for i, e in enumerate(l):
                res += e * 10 ** (len(l) - i - 1)
            return int(res)

        res_list: List[int] = []
        pts = np.argwhere(dg)
        while pts.size > 0:
            id_c, id_l = np.argmax(pts[:, 1]), np.argmax(pts[:, 0])
            column_ele, line_ele = pts[id_c], pts[id_l]
            mask = np.ones(pts.shape[0], dtype=bool)
            mask[id_c] = False
            if np.all(column_ele == line_ele):
                res_list.append(1)
            else:
                res_list.append(2)
                mask[id_l] = False
            pts = pts[mask]
        return list_to_int(res_list)

    p: List[int] = [0] * (perm.size + 1)
    q: List[int] = [0] * (perm.size + 1)
    p[1], q[1] = 1, 1
    p[-1] = compute_fibo_node(perm.matrix)
    q[-1] = p[-1]
    for i in range(perm.size, 1, -1):
        p[i] = compute_fibo_node(perm.matrix[:, :i])
        q[i] = compute_fibo_node(perm.matrix[:i, :])
    return q, p


def permutation_to_growth_diagram(p: Permutation) -> np.ndarray:
    """Fomin's algorithm.
    Relation: permutation p -> growth diagram g_diagram

    >>> permutation_to_growth_diagram(Permutation([2, 7, 1, 5, 6, 4, 3]))
    array([[   0,    0,    0,    0,    0,    0,    0,    0],
           [   0,    0,    0,    1,    1,    1,    1,    1],
           [   0,    1,    1,    2,    2,    2,    2,    2],
           [   0,    1,    1,    2,    2,    2,    2,   12],
           [   0,    1,    1,    2,    2,    2,   12,   22],
           [   0,    1,    1,    2,   12,   12,   22,  212],
           [   0,    1,    1,    2,   12,  112,  212,  222],
           [   0,    1,   11,   21,   22,  212, 2112, 2212]])
    """

    def g_diagram_rules(g_diagram: np.ndarray, i: int, j: int, p: Permutation) -> int:
        mu1, mu2, nu = g_diagram[i, j - 1], g_diagram[i - 1, j], g_diagram[i - 1, j - 1]
        if mu1 == nu:
            if mu2 == nu:
                if p[j] == i:
                    return 1 if nu == 0 else int("1" + str(nu))
                return nu
            return mu2
        if mu2 == nu:
            return mu1
        return 2 if nu == 0 else int("2" + str(nu))

    g_diagram: np.ndarray = np.zeros((p.size + 1, p.size + 1), dtype=int)
    for i in range(1, p.size + 1):
        for j in range(1, p.size + 1):
            g_diagram[i, j] = g_diagram_rules(g_diagram, i, j, p)
    return g_diagram


def permutation_to_chains_gd(p: Permutation) -> Tuple[Chain, Chain]:
    """Fomin's algorithm to obtain pair of chains in the Young-Fibonacci lattice from permutation.
    This version uses the growth diagram.

    Relation: permutation p -> Young-Fibonacci lattice chains (chain1, chain2)
    """
    g_diagram: np.ndarray = permutation_to_growth_diagram(p)
    return g_diagram[:, -1].tolist(), g_diagram[-1, :].tolist()


def chains_to_growth_diagram(c1: Chain, c2: Chain) -> Tuple[np.ndarray, Permutation]:
    """Reverse Fomin's algorithm.
    Relation: Young-Fibonacci lattice chains (c1, c2) -> growth diagram g_diagram, Permutaion p
    """

    def g_diagram_rules_reversed(
        g_diagram: np.ndarray, i: int, j: int
    ) -> Tuple[int, bool]:
        mu1, mu2, lmbda = (
            g_diagram[i + 1, j],
            g_diagram[i, j + 1],
            g_diagram[i + 1, j + 1],
        )
        if lmbda == mu1:
            if lmbda == mu2:
                return lmbda, False
            return mu2, False
        if lmbda == mu2:
            return mu1, False
        w = 0 if lmbda == 1 or lmbda == 2 else int(str(lmbda)[1:])
        if w == mu1:
            return w, True
        return w, False

    n = len(c1)
    g_diagram: np.ndarray = np.zeros((n, n), dtype=int)
    g_diagram[:, -1] = c1
    g_diagram[-1, :] = c2
    t = [0] * (n - 1)
    for i in range(n - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            g_diagram[i, j], x = g_diagram_rules_reversed(g_diagram, i, j)
            if x:
                t[j] = i + 1
    return g_diagram, Permutation(t)


def chain_to_standard_YFT(c: Chain) -> STableau:
    """Janvier's algorithm to obtain Young-Fibonacci Standard Tableau (YFST) from a chain in the Y-F lattice.
    YFST are defined as follow:
        - strictly increasing in columns
        - top row is decreasing
    Relation: Young Fibonacci lattice chain c -> Standard Young Fibonacci Tableau res
    0 stands for empty value.

    >>> chain_to_standard_YFT([0, 1, 2, 12, 22, 221, 2211, 21211])
    ([3, 6, 1, 4, 2], [7, 0, 5, 0, 0])

    >>> chain_to_standard_YFT([0, 1, 11, 21, 22, 212, 2112, 2212])
    ([2, 5, 4, 1], [7, 6, 0, 3])
    """

    def shift(tab: STableau, id_row: int, act: int, end: int) -> None:
        if act == end:
            tab[id_row][end] = 0
            return
        tab[id_row][act] = tab[id_row][act - 1]
        return shift(tab, id_row, act - 1, end)

    def standard_tab_rules(
        prev: List[int], act: List[int], tab: STableau, e: int
    ) -> None:
        def insert_sorted(tab: STableau, id_digit: int, element: int) -> None:
            if id_digit == 0 or tab[1][id_digit - 1] > element:  # trie
                tab[1][id_digit] = element
            else:
                tab[1][id_digit] = tab[1][id_digit - 1]
                return insert_sorted(tab, id_digit - 1, element)
            return

        if len(act) == len(prev):  # transformation du premier un en deux
            for id_digit, digit in enumerate(prev):
                if digit == 1:
                    insert_sorted(tab, id_digit, e)
                    return
        else:  # ajout d'un un (premier un)
            last = len(tab[0]) - 1
            for id_digit, digit in enumerate(act):
                if digit == 1:
                    if id_digit == 0:
                        shift(tab, 0, last, 0)
                        shift(tab, 1, last, 0)
                        tab[0][0] = e
                        return
                    shift(tab, 0, last, id_digit)
                    shift(tab, 1, last, id_digit)
                    tab[0][id_digit] = res[1][id_digit - 1]
                    shift(tab, 1, id_digit - 1, 0)
                    tab[1][0] = e
                    return

    res: STableau = ([0] * len(str(c[-1])), [0] * len(str(c[-1])))
    if len(res[0]) == 1:
        return res
    res[0][0] = 1
    prev = [1]
    for i in range(2, len(c)):
        act = [int(k) for k in str(c[i])]
        standard_tab_rules(prev, act, res, i)
        prev = act
    return res


def standard_YFT_to_chain(std_tab: STableau) -> Chain:
    """Janvier's algorithm reversed.
    Relation: Standard Young Fibonacci Tableau std_tab -> Young Fibonacci lattice chain res
    0 stands for empty

    >>> standard_YFT_to_chain(([3, 6, 1, 4, 2], [7, 0, 5, 0, 0]))
    [0, 1, 2, 12, 22, 221, 2211, 21211]
    """

    def translate_form(tab: STableau) -> int:
        res = 0
        for i in range(len(tab[0])):
            if tab[0][i] != 0 and tab[1][i] != 0:
                    res = res * 10 + 2
            elif tab[0][i] != 0 or tab[1][i] != 0:
                    res = res * 10 + 1
        return res

    def right_neighbor(tab: STableau, pos: int) -> int:
        pos += 1
        while len(tab[1]) > pos+1 and tab[1][pos] == 0:
            pos += 1
        return pos
    
    def apply_reverse_janvier(tab: STableau, pos: int) -> None:
        if tab[1][pos] == 0:
            tab[0].pop(pos)
            tab[1].pop(pos)
            return
        if len(tab[1]) == pos+1:
            tab[1][pos] = 0
            return
        id_neighbor = right_neighbor(tab, pos)
        neighbor = 0 if len(tab[1]) == id_neighbor else tab[1][id_neighbor]            
        if tab[0][pos] > tab[0][pos+1]:
            if tab[0][pos] > neighbor: # cas en bas est le plus grand
                tab[1][pos] = 0
            else: # cas voisin est le plus grand (1)
                tab[1][pos] = neighbor
                apply_reverse_janvier(tab, pos+1)
        else:
            if tab[0][pos+1] > neighbor: # cas coin est le plus grand
                tab[1][pos] = tab[0][pos+1]
                apply_reverse_janvier(tab, pos+1)
            else: # cas voisin est le plus grand (2)
                tab[1][pos] = neighbor
                apply_reverse_janvier(tab, pos+1)

    k = std_tab[0][0] if std_tab[1][0] == 0 else std_tab[1][0]
    res: Chain = [0] * (k + 1)
    if len(res) > 1:
        res[1] = 1
    while len(std_tab[0]) > 0 and k >0:
        res[k] = translate_form(std_tab)
        apply_reverse_janvier(std_tab, 0)
        k -= 1
    return res


def janvier_insertion(p: Permutation) -> Tuple[STableau, STableau]:
    """Janvier's modifications of Roby's insertion algorithm
    Relation: Permutation p -> Pair of Standard Young Fibonacci Tableau (std1, std2)

    >>> janvier_insertion(Permutation([2, 7, 1, 5, 6, 4, 3]))
    (([3, 4, 5, 1], [7, 6, 0, 2]), ([2, 5, 4, 1], [7, 6, 0, 3]))
    """

    def max_not_blacklisted(p: Permutation, blacklist: List[int]) -> Tuple[int, int]:
        res, id_res = 0, 0
        for i in p.keys:
            if not i in blacklist and p[i] > res:
                res, id_res = p[i], i
        return res, id_res

    blacklist_id: List[int] = []
    std1: STableau = ([], [])
    std2: STableau = ([], [])
    for i in range(p.size, 0, -1):
        if not i in blacklist_id:
            m, id_m = max_not_blacklisted(p, blacklist_id)
            blacklist_id.append(i)
            if id_m != i:
                blacklist_id.append(id_m)
                std1[0].append(p[i])
                std1[1].append(m)
                std2[0].append(id_m)
                std2[1].append(i)
            else:
                std1[0].append(p[i])
                std1[1].append(0)
                std2[0].append(i)
                std2[1].append(0)
    return std1, std2
