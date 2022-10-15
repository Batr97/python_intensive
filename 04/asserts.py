from Customlist import Customlist


lst1 = Customlist([1, 2, 3, 4, 10])
lst2 = Customlist([4, 5, 6])
a = (lst1 > lst2)
assert a is True
a = (lst1 < lst2)
assert a is False
a = (lst1 == lst2)
assert a is False

lst1 = Customlist([1, 2, 3, 4])
lst2 = Customlist([4, 5, 6])
a = (lst1 + lst2)
assert a == Customlist([5, 7, 9, 4])
a = (lst1 - lst2)
assert a == Customlist([-3, -3, -3, 4])
a = (lst2 - lst1)
assert a == Customlist([3, 3, 3, -4])

lst1 = [1, 2, 3, 4]
lst2 = Customlist([4, 5, 6])
a = (lst1 + lst2)
assert a == Customlist([5, 7, 9, 4])
a = (lst2 + lst1)
assert a == Customlist([5, 7, 9, 4])
a = (lst1 - lst2)
assert a == Customlist([-3, -3, -3, 4])
a = (lst2 - lst1)
assert a == Customlist([3, 3, 3, -4])
