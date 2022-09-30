def zer(lst):
    for i in range(len(lst)):
        lst[i] = abs(lst[i])
    return(lst)
def close(lst):
    new_lst = [lst[0]]
    i = 1
    while lst[i] == lst[i-1]:
        new_lst.append(lst[i])
        i += 1
    return new_lst
lst = [-1,-1,1,2,-1,3]
# print(*zer(lst))
# print(*close(zer(lst)))