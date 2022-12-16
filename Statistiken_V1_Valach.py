# Patrik Valach
import random
# median
size = 100
num = [random.randrange(1, 101) for i in range(size)]

num.sort()
if size % 2 == 0:
    print((num[size//2] + num[size//2 + 1]) /2)
else:
    print(num[size//2])


# arit

size = 100
num = [random.randrange(1, 101) for i in range(size)]

scit = 0
for i in num:
    scit += i
print(scit/len(num))
