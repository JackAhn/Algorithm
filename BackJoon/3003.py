basic = [1, 1, 2, 2, 2, 8]
user = list(map(int, input().split()))

#두 개 리스트 한 번에 합친 후 연산
result = [a - b for a, b in zip(basic, user)]

#리스트 대괄호 없이 출력
print(*result)
