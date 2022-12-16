import random
# 97 122
array = []
for i in range(20):
    array.append([chr(random.randrange(97, 123)),
                  chr(random.randrange(97, 123)),
                  chr(random.randrange(97, 105)),
                  random.randrange(25, 100)])
print(array)
