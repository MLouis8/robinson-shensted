from Permutation import Permutation
import numpy as np

def roby_insertion(perm):
    """Computes the Roby insertion algorithm on a permutation

    >>> roby_insertion(Permutation([2, 7, 1, 5, 6, 4, 3]))
    ([[7, 6, 5, 2], [3, 4, None, 1]], [[2, 6, 5, 1], [3, 7, None, 4]])
    """
    p, q = [[], []], [[], []]
    for k in perm.keys:
        e = perm[k]
        insert(e, k, p, q, 0)
    return p, q

def shift(p, q, start):
    p[0].append(p[0][-1])
    p[1].append(p[1][-1])
    q[0].append(q[0][-1])
    q[1].append(q[1][-1])
    p[0][-2], p[1][-2] = None, None
    q[0][-2], q[1][-2] = None, None
    for i in range(len(p[0])-2, start, -1):
        p[0][i] = p[0][i-1]
        p[1][i] = p[1][i-1]
        q[0][i] = q[0][i-1]
        q[1][i] = q[1][i-1]

def insert(e, key, p, q, id_c):
    if (len(p[0]) <= id_c):
        p[0].append(e)
        p[1].append(None)
        q[0].append(key)
        q[1].append(None)
    elif e > p[0][id_c]:
        shift(p, q, id_c)
        p[0][id_c] = e
        q[0][id_c] = key
    else:
        if p[1][id_c]:
            tmp = p[1][id_c]
            p[1][id_c] = e
            insert(tmp, key, p, q, id_c+1)
        else:
            p[1][id_c] = e
            q[1][id_c] = key

def evacuation(p):
    """Returns P, the path table from the involution table. 
    Attention on suppose ici que p[0][0] contienne le nombre d'elements de p

    >>> evacuation([[7, 6, 5, 2], [3, 4, None, 1]])
    [[3, 5, 7, 1], [4, 6, None, 2]]
    """
    p_transformed = [[None]*len(p[0]), [None]*len(p[1])]
    for i in range(p[0][0]):
        e, x, y = find_evac_point(p)
        p_transformed[x][y] = e
    return p_transformed

def compare_neighbors(i, j, p):
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

def find_evac_point(p):
    j = 0
    while p[0][j] is None:
        j += 1
    tmp = p[0][j]
    x, y = compare_neighbors(0, j, p)
    return tmp, x, y

def fomin_rules_reversed(g_diagram, i, j):
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

def fomin_rules(g_diagram, i, j, p):
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

def permu_to_y_f_path(permutation):
    """Returns (P1, Q1), paths in the YF graphs, using Fomin's algorithm
    """
    g_diagram = permu_to_growth_diagram(permutation)
    return g_diagram[:, -1], g_diagram[-1, :]

def permu_to_growth_diagram(permutation):
    """Creates growth diagram from permutation

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
    g_diagram = np.zeros((permutation.size+1, permutation.size+1), dtype=int)
    for i in range(1, permutation.size+1):
        for j in range(1, permutation.size+1):
            g_diagram[i, j] = fomin_rules(g_diagram, i, j, permutation)
    return g_diagram

def paths_to_growth_diagram(p1, p2):
    """Creates a growth diagram and a Permutation from a pair of paths in the Y-F lattice
    """
    n = len(p1)
    g_diagram = np.zeros((n, n), dtype=int)
    g_diagram[:, -1] = p1
    g_diagram[-1, :] = p2
    t = [0] * (n-1)
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            g_diagram[i, j], x = fomin_rules_reversed(g_diagram, i, j)
            if x:
                t[j] = i+1
    return g_diagram, Permutation(t)


def paths_to_permu(p1, p2):
    """Creates permutation from a pair of paths in the Y-F lattice
    (version opti sans stockage du gd)
    """
    return

def compare_pred(a, b, k, l):
    print('here', a, b, k, l)
    print(f"a[k]: {a[k]}; b[k]: {b[k]}")
    match a[k]:
        case 1:
            if b[k] == 2 or b[k] == 0: #ajout d'un 1
                a[k] = 0
                return 0, k, a
            return compare_pred(a, b, k+1, l+1)
        case 2:
            if b[k] == 1 or b[k] == 0: #transformation d'un 1
                a[k] = 1
                return 1, k, a
            else:
                return compare_pred(a, b, k+1, l+1)
    return compare_pred(a, b, k+1, l)

def compute_path_table(p):
    """Returns path table from path
    """
    act = [int(i) for i in str(p[-1])]
    tab = [[None]* len(p), [None]* len(p)]
    s = sum(act)
    for k in range(-2, -len(p), -1):
        print(f"round {k}")
        i, j, act = compare_pred(act, [int(h) for h in str(p[k])], 0, 0)
        tab[i][j] = s
        s -= 1
    return tab


def reversed_evacuation(p_tilda):
    """Return p the involution table from p~, the path table
    """
    return