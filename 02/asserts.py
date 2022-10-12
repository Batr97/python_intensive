from close_to_zero import zer, close
from merge import merge

lst = [-5,9,6,-8]
assert zer(lst) == [5,9,6,8]
assert close(lst, zer(lst)) == [-5]
lst =  [-1, 2, -5, 1, -1]
assert zer(lst) == [1,2,5,1,1]
assert close(lst, zer(lst)) == [-1,1,-1]


lst1 = [1, 1, 10, 5]
lst2 = [1, 2, 5, 10, 0]

assert merge(lst1, lst2) == [1, 5, 10]

lst1 = [1, 1, 10, 1, 150, 3]
lst2 = [1, 3, 3, 2, 5, 10, 150]

assert merge(lst1, lst2) == [1, 3, 10, 150]
