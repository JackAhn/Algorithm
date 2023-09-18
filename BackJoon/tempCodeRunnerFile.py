n = int(input())

line = n * 2 - 1
arr = [[' ' for j in range(line)] for i in range(line)]

center = int(line / 2) - 1
start = center
end = center
z = 1
print(center)

for i in range(line) :
    for j in range(start, end) :
        arr[i][j] = '*'
    if start == 0 :
        z *= -1
    start = start - z
    end = end + z
    

for i in range(line) :
    for j in range(line)  :
        print(arr[i][j], end=' ')
    print()
