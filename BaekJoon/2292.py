n = int(input())
cnt = 0
num = 0

while True:
    n = n - 1 if num == 0 else n - (6 * num)
    if n <= 0:
        break
    cnt = cnt + 1
    num = num + 1

print(cnt + 1)
