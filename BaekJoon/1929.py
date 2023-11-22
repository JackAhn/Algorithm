# import random

# global mylist, c
# mylist = []
# c = 1

# def checkNumber(tmp) :
#     if tmp == 1 :
#         return
#     global mylist, c
#     if tmp == 2 :
#         mylist.append(tmp)
#     elif tmp == 3 or tmp == 5 or tmp == 7 :
#         c = 2
#         mylist.append(tmp)
#     else :
#         if (tmp % 2 != 0) and (tmp % 3 != 0) and (tmp % 5 != 0) and (tmp % 7 != 0) :
#             mylist.append(tmp)

# # m, n = input().split(' ')

# m = random.randint(1, 300)
# n = random.randint(m, 300)

# if m == n :
#     checkNumber(m)
# else :
#     for tmp in range(m, n, c) :
#         checkNumber(tmp)
            
# for tmp in mylist :
#     print(tmp)


def test(start, num) :
    #소수 판별하기
    #에라토스테네스의 체 이용
    
    endNum = num + 1
    arr : bool = [0 for i in range(endNum)]

    for i in arr :
        i = False

    for i in range(0, endNum) :
        if i == 0 or i == 1 :
            arr[i] = True
            continue

        if arr[i] == False :
            for j in range(i + i, endNum, i) :
                arr[j] = True
    
    for i in range(start, endNum) :
        if arr[i] == False :
            print(i)
        
m, n = input().split(' ')

m = int(m)
n = int(n)

test(m, n)