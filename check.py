# Checking functions, to assure objects respect certain characteristics


def check_young_fibo_path(p):
    if not isinstance(p, list):
        raise TypeError("Path must be a list of int.")
    if len(p) < 1:
        raise ValueError("Path must contain at least the empty path.")
    if p[0] != 0:
        raise ValueError("Path must start with 0.")
    prev = str(p[0])
    for i in range(1, len(p)):
        act = str(p[i])
        if len(act) == len(prev): #le premier 1 fut remplace par un deux
            flag = False
            for k, c in enumerate(act):
                if prev[k] != 1 and prev[k] != 2:
                    raise ValueError("Numbers must be 1 or 2.")
                if prev[k] != c:
                    if flag or prev[k] == 2:
                        raise ValueError("The path doesn't respect lattice rules.")
                    flag = True
        else: #insertion d'un 1 quelque part
            cpt_1_act, cpt_1_prev, cpt_2_act, cpt_2_prev = 0, 0, 0, 0
            for k, c in enumerate(act):
                if c == 1:
                    cpt_1_act += 1
                elif c == 2:
                    cpt_2_act += 1
                if prev[k] == 1:
                    cpt_1_prev += 1
                elif prev[k] == 2:
                    cpt_2_prev += 1
                else:
                    raise ValueError("Numbers must be 1 or 2.")
            if cpt_2_act != cpt_2_prev or cpt_1_prev + 1 != cpt_1_act:
                raise ValueError("The path doesn't respect lattice rules.")
                

def check_young_fibo_paths(p1, p2):
    check_young_fibo_path(p1)
    check_young_fibo_path(p2)
    if p1[-1] != p2[-1]:
        raise ValueError("Pair of path must end with the same value.")

def check_involution(inv):
    def is_sorted(l):
        temp == l[0]
        for i in l:
            if i < temp:
                return False
            temp = i
        return True
    if not isinstance(inv, list):
        raise TypeError("Involution must be a list.")
    if len(inv) != 2:
        raise TypeError("Involution must contain only two lines.")
    if len(inv[0] != inv[1]):
        raise TypeError("The lines must have the same form.")
    if not is_sorted(inv[1]):
        raise ValueError("The second line must be in decreasing order.")
    for i in range(len(inv[0])):
        if inv[0][i] >= inv[1][i]:
            raise ValueError("Each column must be strictly sorted.")