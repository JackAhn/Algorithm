n, m = map(int, input().split())

myList = []

for i in range(0, n) :
    myList.append(i + 1)
    

for i in range(m) :
    left, right = map(int, input().split())
    temp = myList[left - 1]
    myList[left - 1] = myList[right - 1]
    myList[right - 1] = temp
    
print(*myList)