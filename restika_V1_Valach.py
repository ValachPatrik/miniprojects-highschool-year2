# Patrik Valach

def where_sit(stoly):
    s_pos = None
    obsadenych = 0
    medzery = []
    for i in range(len(stoly)):
        if stoly[i] == 1:
            obsadenych += 1
            if s_pos == None:
                s_pos = i
            else:
                medzery.append([s_pos+1, i-s_pos - 1])
                s_pos = i
    if obsadenych == 0:
        sit_index = -2
    elif obsadenych == 1:
        sit_index = 1
    else:
        max_i = [0, 0]
        for i in range(len(medzery)):
            if medzery[i][1] <= 2:
                continue
            if medzery[i][1] >= max_i[1]:
                max_i = medzery[i]
        if max_i[0] != 0:
            if max_i[1] % 2 == 0:
                sit_index = max_i[0] + max_i[1]//2
            else:
                sit_index = max_i[0] + max_i[1]//2
        else:
            sit_index = None
    return sit_index    
        

stoly = ['x']
[stoly.append(0) for i in range(10)]
stoly.append('x')

for i in range(7):
    where = where_sit(stoly)
    if where:
        if where < 0:
            where = len(stoly) + where
        stoly[where] = 1
        print(where)
    else:
        print('full')
    print(stoly)
