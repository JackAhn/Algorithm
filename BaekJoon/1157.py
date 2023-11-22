s = input()

#대문자로 변환
s = s.upper()

prevCnt = 0
sameCnt = 0
result = ''

#1. 집합
# 중복 값 제거, 순서는 보장 못함
tmpList = set(s)

#2. 딕셔너리
# 리스트 값을 키 값으로 이용하여 딕셔너리로 만든 후, 리스트로 다시 생성
# 키 값이 중복되면 안되기에 중복값이 자연스레 제거됨, 순서도 보장됨
# tmpList = dict.fromkeys(s)
# tmpList = list(tmpList)


for t in tmpList :
    cnt = s.count(t)
    if prevCnt < cnt :
        sameCnt = 0
        prevCnt = cnt
        result = t
    elif prevCnt == cnt :
        sameCnt += 1

if sameCnt > 0 :
    print('?')
else :
    print(result)