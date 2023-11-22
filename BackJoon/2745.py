tmp, p = input().split()

# 기존 풀이 과정
# p = int(p)
# n = len(tmp) - 1
# result = 0
#
# for s in tmp:
#     point = 1 if n == 0 else p ** n
#     num = 0
#     if ord(s) >= 65:
#         num = (ord(s) - 55) * point
#     else:
#         num = int(s) * point
#
#     result = result + num
#     n -= 1

# 추가 풀이
# int(문자열, 진수법) 함수 사용
# 진수법 - 10이 기본값, 2 ~ 36 사이의 값을 입력할 수 있음
print(int(tmp, int(p)))
