arr = [[0 for j in range(9)] for i in range(9)]

for i in range(9):
    arr[i] = list(map(int, input().split()))

row = 0
col = 0
max = -1

for i in range(9):
    for j in range(9):
        if arr[i][j] >= max:
            max = arr[i][j]
            row = i + 1
            col = j + 1

print(max)
print("%d %d" %(row, col))
