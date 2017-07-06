def mapTuples(x):
    t = tuple(map(int, x[0].split(',')))
    return t

def mapcombine(x):
    t = tuple(map(int, x[0].split(',')))
    d = {}
    d[t] = map(int, x[1])
    return d

def mapValueArrays(x):
    d = map(int, x[1])
    d.append(None)
    return d