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