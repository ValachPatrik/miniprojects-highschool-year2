# Patrik Valach
# mas slovnik a zistujes ci su nejake z nich anagramy
dict1 = ['ano', 'nie', 'mozno', 'asi', 'neviem', 'jasne', 'pravdepodobne', 'hej', 'jo', 'oj', 'isa', 'sia']

dictionaries = []
for i in dict1:
    letters = {}
    for j in i:
        letters[j] = (i.count(j)) 
    dictionaries.append(letters)
    print(letters)
indexes = []
for dic in dictionaries:
    ind = [i for i,x in enumerate(dictionaries) if x==dic]
    if len(ind) > 1 and ind not in indexes:
        indexes.append(ind)
for i in indexes:
    print(i, dict1[i[0]])