from Permutation import Permutation
import numpy as np

def roby_insertion(p: Permutation) -> tuple[list, list]:
    """Roby's Insertion algorithm.
    Relation: Permutation p -> involutions (inv1, inv2)

    >>> roby_insertion(Permutation([2, 7, 1, 5, 6, 4, 3]))
    ([[7, 6, 5, 2], [3, 4, None, 1]], [[2, 6, 5, 1], [3, 7, None, 4]])
    """
    def insert(e: int, key: int, inv1: list, inv2: list, id_c: int) -> None:
        def shift(inv1: list, inv2: list, start: int) -> None:
            inv1[0].append(inv1[0][-1])
            inv1[1].append(inv1[1][-1])
            inv2[0].append(inv2[0][-1])
            inv2[1].append(inv2[1][-1])
            inv1[0][-2], inv1[1][-2] = None, None
            inv2[0][-2], inv2[1][-2] = None, None
            for i in range(len(inv1[0])-2, start, -1):
                inv1[0][i] = inv1[0][i-1]
                inv1[1][i] = inv1[1][i-1]
                inv2[0][i] = inv2[0][i-1]
                inv2[1][i] = inv2[1][i-1]

        if (len(inv1[0]) <= id_c):
            inv1[0].append(e)
            inv1[1].append(None)
            inv2[0].append(key)
            inv2[1].append(None)
        elif e > inv1[0][id_c]:
            shift(inv1, inv2, id_c)
            inv1[0][id_c] = e
            inv2[0][id_c] = key
        else:
            if inv1[1][id_c]:
                tmp = inv1[1][id_c]
                inv1[1][id_c] = e
                insert(tmp, key, inv1, inv2, id_c+1)
            else:
                inv1[1][id_c] = e
                inv2[1][id_c] = key
    inv1, inv2 = [[], []], [[], []]
    for k in p.keys:
        e = p[k]
        insert(e, k, inv1, inv2, 0)
    return inv1, inv2

def evacuation(inv: list) -> list:
    """Roby's evacuation algorithm.
    Relation: involution inv -> path tableau
    
    Attention on suppose ici que p[0][0] contienne le nombre d'elements de p

    >>> evacuation([[7, 6, 5, 2], [3, 4, None, 1]])
    [[3, 5, 7, 1], [4, 6, None, 2]]
    """
    def find_evac_point(p: list) -> tuple[int, int, int]:
        def compare_neighbors(i: int, j: int, p: list) -> tuple[int, int]:
            if p[i+1][j] == None: #ligne dessus vide
                p[i][j] = None
                return i, j
            if len(p[i]) <= j+1 or p[i][j+1] == None or p[i+1][j] > p[i][j+1]: #fin de la liste ou voisin droite vide ou voisin dessus > voisin droite
                p[i][j] = p[i+1][j]
                p[i+1][j] = None
                return i+1, j
            else: #voisin dessus <= voisin droite
                p[i][j] = p[i][j+1]
                p[i][j+1] = None
                return compare_neighbors(i, j+1, p)
        j = 0
        while p[0][j] is None:
            j += 1
        tmp = p[0][j]
        x, y = compare_neighbors(0, j, p)
        return tmp, x, y
    path_tableau = [[None]*len(inv[0]), [None]*len(inv[1])]
    for i in range(inv[0][0]):
        e, x, y = find_evac_point(inv)
        path_tableau[x][y] = e
    return path_tableau

def permu_to_growth_diagram(p: Permutation) -> list:
    """Fomin's algorithm.
    Relation: permutation p -> growth diagram g_diagram

    >>> permu_to_growth_diagram(Permutation([2, 7, 1, 5, 6, 4, 3]))
    array([[   0,    0,    0,    0,    0,    0,    0,    0],
           [   0,    0,    0,    1,    1,    1,    1,    1],
           [   0,    1,    1,    2,    2,    2,    2,    2],
           [   0,    1,    1,    2,    2,    2,    2,   12],
           [   0,    1,    1,    2,    2,    2,   12,   22],
           [   0,    1,    1,    2,   12,   12,   22,  212],
           [   0,    1,    1,    2,   12,  112,  212,  222],
           [   0,    1,   11,   21,   22,  212, 2112, 2212]])
    """
    def g_diagram_rules(g_diagram: list, i: int, j: int, p: Permutation) -> int:
        mu1, mu2, nu = g_diagram[i, j-1], g_diagram[i-1, j], g_diagram[i-1, j-1]
        if mu1 == nu:
            if mu2 == nu:
                if p[j]==i:
                    return 1 if nu==0 else int('1'+ str(nu))
                return nu
            return mu2
        if mu2 == nu:
            return mu1
        return 2 if nu == 0 else int('2'+ str(nu))

    g_diagram = np.zeros((p.size+1, p.size+1), dtype=int)
    for i in range(1, p.size+1):
        for j in range(1, p.size+1):
            g_diagram[i, j] = g_diagram_rules(g_diagram, i, j, p)
    return g_diagram

def permutation_to_paths_gd(p: Permutation) -> tuple[list, list]:
    """Fomin's algorithm to obtain pair of paths in the Young-Fibonacci lattice from permutation.
    This version uses the growth diagram.

    Relation: permutation p -> Young-Fibonacci lattice paths (path1, path2)
    """
    g_diagram = permu_to_growth_diagram(p)
    return g_diagram[:, -1], g_diagram[-1, :]

def paths_to_growth_diagram(p1: list, p2: list) -> tuple[list, Permutation]:
    """Reverse Fomin's algorithm.
    Relation: Young-Fibonacci lattice paths (p1, p2) -> growth diagram g_diagram, Permutaion p
    """
    def g_diagram_rules_reversed(g_diagram: list, i: int, j: int) -> tuple[int, bool]:
        mu1, mu2, lmbda = g_diagram[i+1, j], g_diagram[i, j+1], g_diagram[i+1, j+1]
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
    n = len(p1)
    g_diagram = np.zeros((n, n), dtype=int)
    g_diagram[:, -1] = p1
    g_diagram[-1, :] = p2
    t = [0] * (n-1)
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            g_diagram[i, j], x = g_diagram_rules_reversed(g_diagram, i, j)
            if x:
                t[j] = i+1
    return g_diagram, Permutation(t)

def compute_path_tableau(p: list) -> list:
    """Computes path tableau
    Relation: Young-Fibonacci lattice path p -> path tableau tab

    >>> compute_path_tableau([0, 1, 2, 12, 22, 212, 222, 2212])
    [[3, 5, 7, 1], [4, 6, None, 2]]
    """
    def path_tableau_rules(a: list, b: list, k: int, l: int) -> tuple[int, int, list]:
        match a[k]:
            case 1:
                if b[l] == 2 or b[l] == 0: #ajout d'un 1
                    a[k] = 0
                    return 0, k, a
                return path_tableau_rules(a, b, k+1, l+1)
            case 2:
                if b[l] == 1 or b[l] == 0: #transformation d'un 1
                    a[k] = 1
                    return 1, k, a
                else:
                    return path_tableau_rules(a, b, k+1, l+1)
        return path_tableau_rules(a, b, k+1, l)
    act = [int(i) for i in str(p[-1])]
    tab = [[None]* len(act), [None]* len(act)]
    s = sum(act)
    for k in range(-2, -len(p)-1, -1):
        i, j, act = path_tableau_rules(act, [int(h) for h in str(p[k])], 0, 0)
        tab[i][j] = s
        s -= 1
    return tab

def list_to_int(l):
    res = 0
    for i, e in enumerate(l):
        res += e * 10**(len(l) - i-1)
    return res


def permu_to_path(permutation):
    """Returns pair of paths in the Young-Fibonacci lattice from a permutation, optimized version.
    """
    p, q = [0] * (permutation.size+1), [0] * (permutation.size+1)
    p[1], q[1] = 1, 1
    pts = np.argwhere(permutation.matrix)
    e = []
    while len(pts) > 0:
        id_line = np.argmax(pts[:, 0])
        id_col = np.argmax(pts[:, 1])
        max_line = pts.pop(id_line)
        if id_line == id_col:
            e.append(1)
        else:
            max_col = pts.pop(id_col)
            e.append(2)
    
    ele = list_to_int()
    p[-1], q[-1] = ele, ele
    return p, q