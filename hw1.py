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
print(squ(1,3,4))

def sep(lst):
    chet =[]
    nechet=[]
    for el in lst:
        if (el % 2)==0:
            chet.append(el)
        else:
            nechet.append(el)
    assert len(chet) != 0, 'Нет четных значений'
    assert len(nechet) != 0, 'все значения - четные'
    return (chet, nechet)

print(sep([1,5,5,5,7,9,11,11]))