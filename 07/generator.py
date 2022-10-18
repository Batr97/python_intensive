def gen(words, filename):
    f = open(filename, 'r')
    for i in f:
        for word in words:
            if word in i.strip().split(' '):
                yield i
