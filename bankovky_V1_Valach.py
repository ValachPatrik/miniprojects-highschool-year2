# Patrik Valach
import random

mena = [500, 200, 100, 50, 20, 10, 5, 2, 1, 1/2, 1/5, 1/10, 1/20, 1/50, 1/100]

vyplata = random.randrange(100000) + random.randrange(100)/100
vydane = 0
bankoviek = 0
print(vyplata)
for i in mena:
    bankoviek += (vyplata // i)
    vyplata = round(vyplata - (i * (vyplata // i)), 2)
    print('vyplata', vyplata)
print(bankoviek)
