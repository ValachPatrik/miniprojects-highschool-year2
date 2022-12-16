# Patrik Valach
# budeme sa zakazdym pytat ci dany novy datum narodenia uz mame v liste, ked hej tak spocitaj pocet ludi
# narodeniny berem ako range 1-365
# v pripade ze by som chcel pracovat s datumom tak porebujem dvojicu random generatorov ktory mi vytvori mesiac podla toho aj range na den

import random

def nastupenych(pokusov):
    ludi = []
    for i in range(pokusov):
        skupina = []
        unique = True
        while unique:
            n_cl = random.randrange(1, 366)
            if n_cl not in skupina:
                skupina.append(n_cl)
            else:
                ludi.append(len(skupina) + 1)
                unique = False
    #print(ludi)
    print(f'pokusov: {pokusov}')
    return ludi


def avrg(ludi, pokusov):
    # sucet ludi potreba / pocet pokusov = priemer
    sum_l = sum(i for i in ludi)
    avg = sum_l / pokusov
    print(f'average: {avg}')


def med(ludi, pokusov):
    # median
    sort_l = ludi.sort()
    if pokusov % 2 == 0:
        median = (ludi[pokusov//2] + ludi[pokusov//2 + 1]) / 2
    else:
        median = ludi[pokusov//2]
    print(f'median: {median}')


def max_min(ludi):
    print(f'max: {max(ludi)}')
    print(f'min: {min(ludi)}')


def main():
    pokusov = 10000
    ludi = nastupenych(pokusov)
    avrg(ludi, pokusov)
    med(ludi, pokusov)
    max_min(ludi)

if __name__ == '__main__':
    main()