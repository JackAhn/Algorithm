global cnt
cnt = 0
kg = int(input())

def mod3(n) :
    return int(n / 3)

def checkMod3(n) :
    global cnt
    temp = mod3(n)
    afterTmp = int(n % 3)
    if temp == 0 or afterTmp != 0 :
        cnt = -1
    else :
        cnt = temp

tmp = int(kg / 5)
temp = int(kg % 5)

if tmp == 0 :
    # 5가 안되는 경우
    checkMod3(kg)
else :
    #5로 나눠지는 경우
    cnt = tmp
    
    while True :
        if temp == 0 :
            break
        if cnt == 0 :
            checkMod3(kg)
            break
        
        resultTemp = mod3(temp)
        afterTemp = int(temp % 3)
        
        if resultTemp != 0 and afterTemp == 0 :
            cnt = cnt + resultTemp
            break
        else :        
            cnt = cnt - 1
            temp = temp + 5             

print(cnt)