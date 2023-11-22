# 1차 해결 방안
# n = int(input())
# arr = [[0 for j in range(2)] for i in range(n)]
#
# for i in range(n):
#     arr[i] = list(map(int, input().split()))
#
# arr = list(set(map(tuple, arr)))
# n = len(arr)
# result = 100 * n
#
# for i in range(n):
#     w1 = arr[i][0]
#     h1 = arr[i][1]
#     for j in range(i + 1, n):
#         w2 = arr[j][0]
#         h2 = arr[j][1]
#
#         rw = (min(w1, w2) + 10) - max(w1, w2)
#         rh = (min(h1, h2) + 10) - max(h1, h2)
#
#         print(rw, rh)
#
#         if rw > 0 and rh > 0:
#             result = result - (rw * rh)
#
# print(result)

arr = [[0 for j in range(100)] for i in range(100)]

n = int(input())

for i in range(n):
    n1, n2 = map(int, input().split())
    for j in range(n1, n1 + 10):
        for k in range(n2, n2 + 10):
            arr[j][k] += 1

cnt = 0

for i in range(100):
    for j in range(100):
        if arr[i][j] >= 2:
            cnt += (arr[i][j] - 1)

print((n * 100) - cnt)
