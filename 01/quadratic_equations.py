def squ(a,b,c):
    D = b**2 - 4*a*c
    assert (D >= 0) or (D < 0)
    if D >= 0:
        x1 = (-b + D**(0.5))/2/a
        x2 = (-b - D**(0.5))/2/a
        if x1==x2:
            assert x1==x2
            return (x1,)
        else:
            assert x1 != x2
            return (x1,x2)
    else:
        return None