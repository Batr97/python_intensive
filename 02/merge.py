
def merge(lst1, lst2):
    lst = list(set(lst1) & set(lst2))
    return sorted(lst)
