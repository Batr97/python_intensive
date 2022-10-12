def zer(lst):
    lst_abs = []
    for i in range(len(lst)):
        lst_abs.append(abs(lst[i]))
    return(lst_abs)
def close(lst, lst_abs):
    new_lst = []
    minim = min(lst_abs)
    for i in range(len(lst_abs)):
        if lst_abs[i] == minim:
            new_lst.append(lst[i])
    
    return new_lst
# lst = [-1, 2, -5, 1, -1]
# print(*zer(lst))
# print(*close(lst, zer(lst)))