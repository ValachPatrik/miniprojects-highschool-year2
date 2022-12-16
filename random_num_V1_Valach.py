# Patrik Valach
import random

rmax = 1000000
n = random.randrange(1,rmax)

def ota(n, i):
    if i > n:
        return -1
    elif i < n:
        return +1
    elif i == n:
        return 0

def poc_ot(n, guess, step, rmax, div):
    step += 1
    div = div//2
    if div == 0:
        div = 1
    o = ota(n, guess)
    if o == -1:
        guess = guess - (div)
    elif o == +1:
        guess = guess + (div)
    elif o == 0:
        return step, guess
    return poc_ot(n, guess, step, rmax, div)

def uhadni(n):
    guess = input('Guess a number: ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Not a number')
        return uhadni(n)
    o = ota(n, guess)
    if o == -1:
        print('Smaller')
        return uhadni(n)
    elif o == +1:
        print('Higher')
        return uhadni(n)
    elif o == 0:
        return 'Correct', guess

print(n)
print(poc_ot(n, rmax //2, 1, rmax, rmax//2))
print(uhadni(n))
