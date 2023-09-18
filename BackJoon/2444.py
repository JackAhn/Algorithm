n = int(input())

line = n * 2 - 1
arr = [[' ' for j in range(line)] for i in range(line)]

start = end = int(line / 2)
z = 1

for i in range(line) :
    for j in range(0, end + 1) :
        if j >= start and j <= end :
            print('*', end='')
        else :
            print(' ', end='')
    if start == 0 :
        z *= -1
    start = start - z
    end = end + z
    print()