# 약수들의 합
while True:
    n = int(input())
    if n == -1:
        break

    numList = []
    lNum = -1
    modNum = 2

    while True:
        if lNum != -1 and lNum <= modNum: # 더 이상 나눌 수 없을 때
            break
        if n % modNum == 0:
            lNum = int(n / modNum) # 숫자 나누기
            numList.append(modNum) # 나눈 값 추가
            if lNum != modNum: # 중복된 숫자가 아니면
                numList.append(lNum) # 몫 추가
        modNum = modNum + 1 # 나눌 값 증가

    numList.sort()

    if sum(numList) + 1 == n:
        print(str(n) + ' = 1 + ' + ' + '.join(map(str, numList)))
    else:
        print(str(n) + ' is NOT perfect.')
