# Patrik Valach
# najdite 2 naj N 3-cif. cisla, ktorych sucin je palindrom
# dvojity cyklus ktory bude skusat nasobky 3-cif od naj po najmen a zapameta si tu najvacsiu dvojicu a porovnava ich sucet

def h3palin():
    highst = 0
    ma = 99999
    mi = 9999
    for i in range(ma, mi, -1):
        for j in range(ma, i, -1):
            sucin = i*j
            if str(sucin) == str(sucin)[::-1]:
                #print(i, j, i*j)
                if highst < sucin:
                    highst = sucin
                    hnum = [i, j]
    print(highst)
    print(hnum)

h3palin()

def is_pal(c):
    return int(str(c)[::-1]) == c

def palin(amount_v: int = 2, n_digits: int = 3, val_s: str = 'max', type_op: str = '*', outval: str = 'palindrom'):
    pass