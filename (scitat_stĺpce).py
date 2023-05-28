import random

NUM = 50
COLS = 10
ROWS = NUM // COLS

cols = [[random.randint(0, 9) for _ in range(ROWS)] for _ in range(COLS)]

for col in cols:
    col.sort()

for i in range(ROWS):
    for j in range(COLS):
        print(str(cols[j][i]) + '  ', end='')
    print()       

print('-' * (3*COLS - 1))

for col in cols:
    print("{:<3d}".format(sum(col)), end='')
