# Patrik Valach
# system ktory nemoze mat v premennej vyssie cisla ako 1000
# ako simulovat vacsie cisla
# ako by fungovala +-*/

import math

# cez exp/log prevod
# neprejde to limitom 1000 ale dlzku to presiahne
def num_encode1(a):
    return math.log(a)/math.log(1000)

def num_decode1(a):
    return math.pow(1000, a)

for i in range(1000, 990, -1):
    i = num_encode1(i)
    print(i)
    i = num_decode1(i)
    print(i)

# po tisickach delime cislo do listu a ked dlzka dosiahne limit tak sa zapisuje do dalsieho
# na to aby to bolo naozaj nekonecne tak by sme potrebovali rekurzivnu funkciu ktora by zakazdym urobila dalsi rozmer a vnorila dalsi set listov
def num_encode2(a):
    i = 0
    l = []
    l2 = []
    while a > 0:
        if len(l2) == 1000:
            print('function out of range')
            return l2
        if len(l) == 1000:
            l2.append(l)
            l = []
        i += 1
        l.append(a % (1000))
        a = (a - l[-1]) // 1000
    return l2

def num_decode2(a):
    pass


for i in range(1000**1000000, 1000**1000001, 1000**1000):
    print(i)
    print(num_encode2(i))