# Patrik Valach
# 22.12.2021
# Lists

import random

def print_out(x, ind=None):
    # print out list
    max_l = len(str(max(map(max, x))))
    for i in range(len(x)):
        for j in x[i]:
            print(' ' * (max_l - len(str(j))), end='')
            print(j, end=' ')
        if ind is not None:
            if ind[1] is None:
                ind[1] = len(x[0])
            if (ind[0] - 1) < i < ind[1]:
                print('<<', end='')
        print()
    if ind is not None:
        print((max_l + 1) * ind[0] * ' ', end='')
        print(('|' + (max_l-2) * ' ' + '| ') * (ind[1] - ind[0]), end='')
    print()


def size():
    # get input for size of a two dimensional list
    rows = input('Set number of rows   (def: 10): ')
    columns = input('set number of colums (def: 10): ')
    val = input('Set init value       (def:  0): ')
    if rows == '':
        rows = '10'
    if columns == '':
        columns = '10'
    if val == '':
        val = 0
    if rows.isdigit() and columns.isdigit():
        rows = int(rows)
        columns = int(columns)
    else:
        print('Not a Number, try again.')
        return size()
    if rows <= 0 or columns <= 0:
        print('Negative or Zero number of rows / columns, try again.')
        return size()
    return rows, columns, val


def create(row, col, val):
    # create a two dimensional list with specified size and value
    return [[val for i in range(col)] for i in range(row)]


def random_val():
    # get input for random number range
    minim = input('Set minimum for random range (def:  1): ')
    maxim = input('Set maximum for random range (def: 99): ')
    if minim == '':
        minim = '1'
    if maxim == '':
        maxim = '99' 
    if minim.isdigit() and maxim.isdigit():
        minim = int(minim)
        maxim = int(maxim)
    else:
        print('Not a Number')
        return random_val()
    return minim, maxim


def fill_random(x, val_start, val_end):
    # fill two dimensional list with random values
    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j] = random.randrange(val_start, val_end)
    return x


def sort_val(rows, columns):
    # get input for indexes to sort
    sort_min = input('Sort rows and columns from index (def:   0): ')
    sort_max = input('Sort rows and columns to   index (def: max): ')
    if sort_min == '':
        sort_min = '0'
    if sort_max == '':
        sort_max = None
    if sort_min.isdigit() and (sort_max is None or sort_max.isdigit()):
        sort_min = int(sort_min)
        if sort_max is not None:
            sort_max = int(sort_max) + 1
    else:
        print('Not a Number')
        return sort_val(rows, columns)
    if sort_min < 0 or sort_min > max(rows, columns) or (sort_max is not None and sort_max > max(rows, columns)) or (sort_max is not None and sort_min >= sort_max):
        print('Invalid index')
        return sort_val(rows, columns)
    show = input('Show sorting process? (Y/N) (def: N): ')
    if show == '':
        show = 'N'
    elif show != 'Y' and show != 'N':
        print('Accepts only Y or N.')
        return sort_val(rows, columns)
    return sort_min, sort_max, show


#-----------------------OLD SORTERS (not used)---------------------------------
def sort_self(x, row):
    # sort rows of a two dimensional list and return sorted row - ascending
    x = x[row]
    for j in range(len(x)):
        min_in_list = j
        for k in range(j, len(x)):
            if x[k] < x[min_in_list]:
                min_in_list = k
        x[j], x[min_in_list] = x[min_in_list], x[j]
    return x


def sort_rekurz(d_list, i, row):
    # sort one dimensional list and return sorted row - ascending
    x = d_list[row]
    min_in_list = i
    if i == len(x):
        return d_list[row]
    for k in range(i, len(x)):
        if x[k] < x[min_in_list]:
            min_in_list = k
    x[i], x[min_in_list] = x[min_in_list], x[i]
    d_list[row] = x
    return sort_rekurz(d_list, i+1, row)
#------------------------------------------------------------------------------

def sorter(x, sort_min, sort_max, rc, show):
    # sort row / column range of two dimensional list
    global step_id
    if rc == 'r': # sort rows
        if sort_max is None or sort_max > len(x):
            sort_max = len(x)
        if sort_min >= len(x):
            return x
        for i in range(sort_min, sort_max):
            if show == 'Y':
                print('Sorting row {}'.format(i))
            for j in range(len(x[i])):
                min_index = j
                for k in range(j, len(x[i])):
                    if show == 'Y':
                        print('step {} ; {} ; {} ; {} ; {}'.format(step_id, k, x[i][k], min_index, x[i]))
                        step_id += 1
                    if x[i][k] < x[i][min_index]:
                        min_index = k
                x[i][j], x[i][min_index] = x[i][min_index], x[i][j]
    elif rc == 'c': # sort columns
        if sort_max is None or sort_max > len(x[0]):
            sort_max = len(x[0])
        if sort_min >= len(x[0]):
            return x
        for i in range(sort_min, sort_max):
            if show == 'Y':
                print('Sorting column {}'.format(i))
            for j in range(len(x)):
                min_index = j
                for k in range(j, len(x)):
                    if show == 'Y':
                        print('step {} ; {} ; {} ; {} ; {}'. format(step_id, k, x[k][i], min_index, [x[m][i] for m in range(len(x))]))
                        step_id += 1
                    if x[k][i] < x[min_index][i]:
                        min_index = k
                x[j][i], x[min_index][i] = x[min_index][i], x[j][i]
    return x


def main() -> None:
    global step_id
    # call for empty list
    rows, columns, val = size()
    x = create(rows, columns, val)
    print('Two dimensional field initialization:')
    print_out(x)

    # call to fill with random values
    minim, maxim = random_val()
    x = fill_random(x, minim, maxim)
    print('Two dimensional filed with random numbers from given range:')
    print_out(x)

    # call to sort
    sort_min, sort_max, show = sort_val(rows, columns)
    step_id = 1
    x = sorter(x, sort_min, sort_max, 'r', show)
    x = sorter(x, sort_min, sort_max, 'c', show)
    print('Two dimensional field sorted:')
    print_out(x, [sort_min, sort_max])

if __name__ == '__main__':
    main()
