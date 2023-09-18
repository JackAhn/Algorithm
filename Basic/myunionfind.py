arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def getParent(num) -> int :
    if arr[num] == num :
        return num
    else :
        return getParent(arr[num])

def unionParent(num1, num2) :
    val1 = getParent(num1)
    val2 = getParent(num2)
    
    if val1 < val2 :
        arr[num2] = val1
    else :
        arr[num1] = val2

def findUnion(num1, num2) -> int :
    val1 = getParent(num1)
    val2 = getParent(num2)
    
    if val1 == val2:
        return 1
    else :
        return 0
    

unionParent(1, 5)
print(findUnion(1, 5))
