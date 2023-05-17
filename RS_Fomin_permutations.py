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

def fomin_rules_reversed(g_diagram, i, j, p):
    mu1, mu2, lmbda = g_diagram[i+1, j], g_diagram[i, j+1], g_diagram[i+1, j+1]
    if lmbda == mu1:
        if lmbda == mu2:
            return lmbda, False
        return mu2, False
    if lmbda == mu2:
        return mu1, False
    w = 33333 # tronquer le premier digit
    if w == mu1:
        return w, True
    return w, False

def fomin_rules(g_diagram, i, j, p):
    mu1, mu2, nu = g_diagram[i, j-1], g_diagram[i-1, j], g_diagram[i-1, j-1]
    if mu1 == nu:
        if mu2 == nu:
            if p[j]==i:
                return 1 if nu==0 else nu + 10**(int(np.log10(nu+1))+1)
            return nu
        return mu2
    if mu2 == nu:
        return mu1
    return 2 if nu == 0 else nu + 2*10**(int(np.log10(nu+1))+1)

def permu_to_y_f_path(permutation):
    """Returns (P1, Q1), paths in the YF graphs, using Fomin's algorithm
    """
    g_diagram = permu_to_growth_diagram(permutation)
    return gd[:, -1], gd[-1, :]

def permu_to_growth_diagram(permutation):
    """Creates growth diagram from permutation
    """
    g_diagram = np.zeros((permutation.size+1, permutation.size+1), dtype=int)
    for i in range(1, permutation.size+1):
        for j in range(1, permutation.size+1):
            g_diagram[i, j] = fomin_rules(g_diagram, i, j, permutation)
    return g_diagram

def growth_diagram_to_permu(g_diagram):
    """Create permutation from growth diagram
    """
    pass