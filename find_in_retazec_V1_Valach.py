# Patrik Valach
def find_in_r(r1, r2):
    for i in range(len(r1)):
        for j in range(len(r2)):
            if r1[i+j] != r2[j]:
                break
        else:
            print(r1[i:i+len(r2)], i)


r1 = 'thereisalwaysabiggerfishthisiswherethefunbegginsdoitunlimitedpoweriamthefishsenate'
r2 = 'fish'
find_in_r(r1, r2)