def sep(lst):
    chet =[]
    nechet=[]
    for el in lst:
        if (el % 2)==0:
            chet.append(el)
        else:
            nechet.append(el)
    return (chet, nechet)