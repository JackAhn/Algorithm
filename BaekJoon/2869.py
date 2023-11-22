a, b, v = input().split(' ')

a = int(a)
b = int(b)
v = int(v)

moveCnt = a - b

if moveCnt > 1 :
    moveDay = int(( (v - a) / moveCnt))
    moveOtherDay = int(( (v - a) % moveCnt))
    if  moveOtherDay > 0 :
        moveDay = moveDay + 1
    moveDay = moveDay + 1
else :
    moveDay = v - b

print(moveDay)

# while True :
#     num = num + a
#     print(num)
#     if(num >= v) :
#         break
    
#     num = num - b
#     cnt = cnt + 1
