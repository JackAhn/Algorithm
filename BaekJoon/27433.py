#팩토리얼 2

num = 0
global result
result = 1

def doFactorial(a):
    if a == 0 :
        return
    result *= a
    doFactorial(a - 1)

num = int(input())
doFactorial(num)
print(result)