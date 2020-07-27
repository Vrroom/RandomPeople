from functools import reduce 

def flatten(l) :
    if len(l) == 0 : 
        return []
    else :
        paths1 = list(filter(lambda x: isinstance(x, svg.Path), l))
        paths2 = reduce(lambda a, b: a + b, map(flatten, filter(lambda x : isinstance(x, list), l)), [])
        return paths1 + paths2

