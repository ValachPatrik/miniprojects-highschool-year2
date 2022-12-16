# Patrik Valach
import random


def new_field(n, r_min, r_max):
    if n <= 0:
        return 'Invalid lenght value.'
    return [random.randrange(r_min, r_max + 1) for i in range(n)]


def find_max(nmrs, m):
    if len(nmrs) < m:
        return 'List too small for given range.'
    elif m <= 0:
        return 'Invalid range value.'
    max_i = [None, None, None]
    for k in range(2, m+1):
        for i in range(len(nmrs) - k + 1):
            add = 0
            for j in range(k):
                add += nmrs[i+j]
            if max_i[0] == None:
                max_i[0] = i
                max_i[1] = add
                max_i[2] = k
            else:
                if add >= max_i[1]:
                    max_i[0] = i
                    max_i[1] = add
                    max_i[2] = k
    return ([nmrs[max_i[0] + i] for i in range(max_i[2])], max_i[1])

def invalues():
    n = input('Input list lenght (def=10): ')
    try:
        if n == '':
            n = 10
        n = int(n)
        if n <= 0:
            print('Invalid lenght value, must be possitive.')
            return invalues()
    except:
        print('Lenght must be a number.')
        return invalues()

    r_min = input('Input range minimum (def=-10): ')
    try:
        if r_min == '':
            r_min = -10
        r_min = int(r_min)
    except:
        print('Minimum must be a number.')
        return invalues()

    r_max = input('Input range maximum (def=10): ')
    try:
        if r_max == '':
            r_max = 10
        r_max = int(r_max)
    except:
        print('Maximum must be a number.')
        return invalues()

    if r_max < r_min:
        print('Maximum is bigger than minimum.')
        return invalues()

    return n, r_min, r_max


n, r_min, r_max = invalues()
nmrs = new_field(n, r_min, r_max)
print(nmrs)
max_all = find_max(nmrs, n)
print(f'numbers: {max_all[0]}, sum: {max_all[1]}, lenght: {len(max_all[0])}')