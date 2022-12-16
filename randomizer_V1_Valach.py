# Patrik Valach
import random

def sportka_cisla():
    numb = []
    size = 6
    while len(numb) != size:
        numb.append(random.randrange(1, 49))
    return numb

print(sportka_cisla())

def usporiadanie_random():
    n = random.randrange(1, 100)
    width = 15
    numb = [i for i in range(n, n + width)]
    numb_r = []
    for i in range(width):
        numb_r.append(numb[random.randrange(len(numb))])
        del numb[0]
    return numb_r

print(usporiadanie_random())