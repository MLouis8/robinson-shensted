from typing import List

def robinson_schensted(l: List[int]) -> List[List[int]]:
    """Returns Robinson-Schensted table.

    >>> robinson_schensted([3, 8, 4, 1, 2])
    [[1, 2], [3, 4], [8]]
    
    >>> robinson_schensted('acdbaedbc')
    [['a', 'a', 'b', 'c'], ['b', 'd', 'd'], ['c', 'e']]
    """
    def insert_in_line(e: int, t: List, line_id: int) -> None:
        if (len(t) <= line_id):
            t.append([])
        for i, e1 in enumerate(t[line_id]):
            if e1 > e:
                t[line_id][i] = e
                insert_in_line(e1, t, line_id+1)
                return
        t[line_id].append(e)
    t: List = []
    for e in l:
        insert_in_line(e, t, 0)
    return t

def longueurs_sscsd(l: List[int]) -> List[int]:
    t = robinson_schensted(l)
    return [len(i) for i in t]

def taille_plus_grande_ssc(l: List[int]) -> int:
    return len(robinson_schensted(l)[0])