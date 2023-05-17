def robinson_schensted(l):
    """Returns Robinson-Schensted table.

    >>> robinson_schensted([3, 8, 4, 1, 2])
    [[1, 2], [3, 4], [8]]
    
    >>> robinson_schensted('acdbaedbc')
    [['a', 'a', 'b', 'c'], ['b', 'd', 'd'], ['c', 'e']]
    """
    t = []
    for e in l:
        insert_in_line(e, t, 0)
    return t

def insert_in_line(e, t, line_id):
    if (len(t) <= line_id):
        t.append([])
    for i, e1 in enumerate(t[line_id]):
        if e1 > e:
            t[line_id][i] = e
            insert_in_line(e1, t, line_id+1)
            return
    t[line_id].append(e)

def longueurs_sscsd(l):
    t = robinson_schensted(l)
    return [len(i) for i in t]

def taille_plus_grande_ssc(l):
    return len(robinson_schensted(l)[0])