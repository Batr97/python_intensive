from division_of_list import sep
from quadratic_equations import squ

assert squ(1,3,-4) == (1.0, -4.0)
assert squ(1,3,4) == None

assert sep([1,5,5,5,7,9,11,11]) == ([], [1,5,5,5,7,9,11,11])
assert sep([1,2,4,5,7,9,10,11]) == ([2,4,10], [1,5,7,9,11])