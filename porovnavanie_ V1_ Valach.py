# Patrik Valach

import random

def porovnaj(a, b):
    return max(a, b)

def porovnaj2(a, b):
    if g[a] > g[b]:
        return a
    return b


def utried(g):
    for i in range(len(g)):
        for j in range(len(g)):
            if porovnaj(g[i], g[j]) == g[j]:
                g[j],g[i] = g[i],g[j]
    return index

g = [random.randrange(1, 50) for i in range(10)]
print(g[-1], g[-2])
print(g)


def max_i(g):
    max1 = 0
    max2 = 0
    for i in range(len(g)):
        max2 = porovnaj2(i, max2)
        if porovnaj2(max1, max2) != max1:
            max1, max2 = max2, max1
    return max1, max2

g = [random.randrange(1, 50) for i in range(10)]
print(max_i(g))
print(g)