# Patrik Valach

import random

pole = [i for i in range(20)]
random.shuffle(pole)
print(pole)

prejdene = [] # pozicie co sme uz presli niektorym cyklom
cyklov = 0 # pocet najdenych cyklov
for i in pole:
    if i not in prejdene:
        print('\n novy cyklus', i)
        cyklov += 1
        pos = pole[i]
        prejdene.append(pos)
        while pos != i:
            print(pos, end=' ')
            prejdene.append(pos)
            pos = pole[pos]
        print(pos, end=' ')
        
print('pocet cyklov', cyklov)
            