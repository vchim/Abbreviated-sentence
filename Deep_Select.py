#-*-coding:utf-8-*-

def start_end(list, key, dict):
    '''To fix the start word & end word of sentences'''
    for k in key:
        if dict[k][0] not in list:
            del dict[k]
        elif dict[k][-2] not in list:
            del dict[k]
        elif 'y' in dict[k]:
            del dict[k]
    return dict

def pos_n(list, pos_type):
    for pos in range(len(list)):
        if list[pos] == 'n':
            pos_type = pos
            break
        else:
            continue
    return pos_type

def pos_r(list, pos_type):
    for pos in range(len(list)):
        if list[pos] == 'r':
            pos_type = pos
            break
        else:
            continue
    return pos_type

def pos_v(list, pos_type):
    for pos in range(len(list)):
        if list[pos] == 'v':
            pos_type = pos
            break
        else:
            continue
    return pos_type

def position(key, dict):
    '''To fix the position of verbs'''
    for k in key:
        n_pos = 0
        v_pos = 0
        r_pos = 0
        if ('n' and 'v' in dict[k]) and ('r' not in dict[k]):
            if (pos_v(dict[k], v_pos) - pos_n(dict[k], n_pos)) <= 0:
                del dict[k]
            else:
                continue
        elif ('r' and 'v' in dict[k]) and ('n' not in dict[k]):
            if (pos_v(dict[k], v_pos) - pos_r(dict[k], r_pos)) <= 0:
                del dict[k]
            else:
                continue
        else:
            n_pos = pos_n(dict[k], n_pos)
            v_pos = pos_v(dict[k], v_pos)
            r_pos = pos_r(dict[k], r_pos)
            if n_pos <= r_pos:
                if v_pos <= n_pos:
                    del dict[k]
            else:
                if v_pos <= r_pos:
                    del dict[k]
    return dict
