import random

def initset():
    size = 4
    ppl = [i for i in range(size)]
    likes = []

    for i in ppl:
        for j in ppl:
            if random.randrange(2) == 0:
                likes.append([i, j])
    print(likes)
    return size, likes

size, likes = initset()

# how many others like x
def a(likes, x):
    ammount = 0
    for i in likes:
        if i[1] == x:
            ammount += 1
    return ammount

print(a(likes, 1))

# how many symetric "like pairs"

def b(likes):
    ammount = 0
    for i in likes:
        if [i[1], i[0]] in likes and i != [i[1], i[0]]:
            ammount += 1
    return ammount // 2

print(b(likes))

# how many transitive triplets

def c(likes):
    ammount = 0
    for i in likes:
        for j in likes:
            for k in likes:
                if i[0] != i[1] and j[0] != j[1] and k[0] != k[1]:
                    if i not in [j, k] and j != k:
                        if i[1] == j[0] and j[1] == k[0] and k[1] == i[0]:
                            ammount += 1
    return ammount // 3

print(c(likes))

# how many transitive quad

def d(likes):
    ammount = 0
    for i in likes:
        for j in likes:
            for k in likes:
                for l in likes:
                    if i[0] != i[1] and j[0] != j[1] and k[0] != k[1] and l[0] != l[1]:
                        if i not in [j, k, l] and j not in [k, l] and k != l:
                            if i[1] == j[0] and j[1] == k[0] and k[1] == l[0] and l[1] == i[0]:
                                ammount += 1
    return ammount // 4

print(d(likes))

# triangular likes

def e(likes, size):
    ammount = 0
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if i != j and i != k and j != k:
                    if [i, j] in likes and [j, i] in likes and [i, k] in likes and [k, i] in likes:
                        ammount += 1
                        print(i, j, k)
    return ammount // 2

print(e(likes, size))

# who is not liked
def f(likes, size):
    notliked = []
    for i in range(size):
        for j in likes:
            if j[1] == i:
                break
        else:
            notliked.append(i)
    return notliked

print(f(likes, size))
