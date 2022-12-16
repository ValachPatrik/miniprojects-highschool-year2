def prvocislo(n):
    if n > 1:
        for i in range (2, n**0.5):
            if (n % i) == 0:
                return False
    return True
cif = int(input('Zadaj počet cifier: '))
n = int(cif * '9')
for i in range(n, 1, -1):
    if prvocislo(i):
        print(i)
        break