n, b = map(int, input().split())
num = n
result = []

while True:
    if num == 0:
        break

    tmp = num % b
    num = int(num / b)

    # 십진수 이하면 그대로 나눈 값 추가
    if tmp < 10:
        result.append(str(tmp))
    # 아니면 아스키 코드 값 추가
    else:
        result.append(chr(55 + tmp))

print(''.join(result.__reversed__()))
