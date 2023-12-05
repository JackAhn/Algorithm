# m = int(input())
# n = int(input())
# prime = [2, 3, 5, 7]  # 기본 소수 (11 이상부터 안걸러짐)
#
# minVal = -1
# sumVal = 0
#
# for i in range(m, n + 1):
#     choice = 0
#     if prime.count(i) > 0:
#         choice = i
#         sumVal += i
#     else:
#         result = list(map(lambda j: i % j, prime))
#         if result.count(0) == 0:
#             print(i)
#             choice = i
#             sumVal += i
#
#     if choice != 0 and (minVal == -1 or minVal > choice):
#         minVal = choice
#
# if minVal != -1:
#     print(sumVal)
# print(minVal)


# 다른 풀이 1
# m = int(input())
# n = int(input())
#
# minVal = -1
# sumVal = 0
#
# if m == 1:
#     m += 1
#
# for i in range(m, n + 1):
#     isPrime = True
#     for j in range(2, i):
#         if i % j == 0:
#             isPrime = False
#             break
#     if isPrime:
#         sumVal += i
#         if minVal == -1:
#             minVal = i
#
# if minVal != -1:
#     print(sumVal)
# print(minVal)

# 다른 풀이 2 - 에라토스테네스의 체
m = int(input())
n = int(input())

primeList = [i for i in range(n + 2)]
primeList[1] = 0

for i in range(2, n + 1):
    if primeList[i] != 0:
        for j in range(i * i, n + 1, i):
            primeList[j] = 0

primeList = list(filter(lambda x: x != 0, primeList[m:(n + 1)]))

sumVal = sum(primeList)

if sumVal == 0:
    print(-1)
else:
    print(sumVal)
    print(min(primeList))

