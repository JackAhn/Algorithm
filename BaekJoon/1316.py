num = int(input())
result = 0
for n in range(num):
    str = input()
    flag = 1
    strCnt = len(str)
    beforeInd = 0
    for i in range(strCnt):
        # c = str[i]
        # cnt = str.count(c, 0, strCnt)
        #
        # if cnt > 1:
        #     tmp = str[i + 1:]
        #     tmp = tmp.replace(c, '', 1)
        #     cnt = tmp.count(str[i], 0, len(tmp))
        #
        # if cnt > 0:
        #     flag = 0
        #     break
        ind = str.rfind(str[i], 0, strCnt)
        for j in range(ind - 1, beforeInd, -1):
            if str[j] != str[i]:
                flag = 0
                break
        if flag == 0:
            break
        i = beforeInd = ind
    result += flag
print(result)