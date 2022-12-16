# Patrik Valach
DN = 4
MN = 7
RN = 1917

DD = 3
DM = 2
DR = 2022

dni = 0
priestupnych = 0

#rok

def priestupny(y):
    global priestupnych
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                priestupnych += 1
                return True
            return False
        priestupnych += 1
        return True
    return False


dni += (DR - RN - 1) * 365
for i in range(DR, RN + 1, -1):
    if priestupny(i):
        dni += 1


# Mesiac

PDM = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(12, MN, -1):
    dni += PDM[i]
    if priestupny(RN) and i == 2:
        dni += 1
for i in range(1, DM):
    dni += PDM[i]
    if priestupny(DR) and i == 2:
        dni += 1


#Dni

dni += PDM[MN] - DN
dni += DD

print(dni)
print(dni//7)
print(priestupnych)