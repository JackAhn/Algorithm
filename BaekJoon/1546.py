cnt = int(input())
scoreList = list(map(int, input().split()))
resultScore = 0

scoreList.sort(reverse = True)

maxScore = scoreList[0]

for i in range(cnt) :
    resultScore = resultScore + (scoreList[i]/maxScore*100)

print(resultScore / cnt)