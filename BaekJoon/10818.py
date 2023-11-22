n = int(input())
temp = list(map(int, input().split()))

temp = sorted(temp)

print("%d %d" %(temp[0], temp[n - 1]))