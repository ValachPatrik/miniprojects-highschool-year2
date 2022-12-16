import random

class game:
    def __init__(self, r_num_max):
        self.r_num = random.randrange(r_num_max)
        print(self.r_num)

    def guess(self, g_num):
        if g_num > self.r_num:
            return -1
        elif g_num < self.r_num:
            return 1
        if g_num == self.r_num:
            return 0

for i in range(1):
    r_num_max = 1000000
    g1 = game(r_num_max)
    l_guess = r_num_max//2
    r = g1.guess(l_guess)
    guessed = [l_guess]
    while r != 0:
        if r == 1:
            l_guess = round(l_guess * 1.5)
        elif r == -1:
            l_guess = round(l_guess * 0.5)
        while l_guess in guessed:
            l_guess += 1
        guessed.append(l_guess)
        r = g1.guess(l_guess)
        print(l_guess)
        print(guessed)
    print(l_guess)
