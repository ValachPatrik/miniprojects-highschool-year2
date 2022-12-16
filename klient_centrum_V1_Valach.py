# Patrik Valach

def vypis(x):
    x = str(x)
    if ('6' in x or '9' in x or '8' in x or '0' in x) and \
            all(j not in x for j in '123457') and \
            (x[-1] != '0'):
        y = x[::-1]
        for j in range(len(y)):
            if y[j] == '6':
                y = y[:j] + '9' + y[j+1:]
            elif y[j] == '9':
                y = y[:j] + '6' + y[j+1:]
        if x != y:
            return f'{x}.'
    return ''

for i in range(1000):
    print(vypis(i), end='')