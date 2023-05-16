from Permutation import Permutation

def roby_insertion(perm):
    p, q = [[], []], [[], []]
    for k in perm._get_keys:
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
    """
    Attention on suppose ici que p[0][0] contienne le nombre d'elements de p
    """
    p_transformed = [[None]*len(p[0]), [None]*len(p[1])]
    for i in range(p[0][0]):
        e, x, y = find_evac_point(p)
        print('kabounga', e, x, y)
        p_transformed[x][y] = e
    return p_transformed

def compare_neighbors(i, j, p):
    print(f"compare {i, j, p}")
    if p[i+1][j] == None: #ligne dessus vide
        print('A', i+1, j)
        p[0].pop(j)
        p[1].pop(j)
        return i, j
    if len(p[i]) <= j+1 or p[i+1][j] > p[i][j+1]: #fin de la liste ou voisin dessus > voisin droite
        p[i][j] = p[i+1][j]
        p[i+1][j] = None
        return i+1, j
    if p[i][j+1] == None:  #voisin droite vide
        print('B')
        p[i][j] = p[i+1][j]
        p[i+1][j] = None
        p[0].pop(j+1)
        p[1].pop(j+1)
        return i+1, j
    else: #voisin dessus <= voisin droite
        print('D', p[i+1][j], p[i][j+1])
        p[i][j] = p[i][j+1]
        p[i][j+1] = None
        return compare_neighbors(i, j+1, p)

def find_evac_point(p):
    tmp = p[0][0]
    x, y = compare_neighbors(0, 0, p)
    print(f"P = {p}")
    return tmp, x, y