a, b, c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

result = 0

if b >= c :
    result = -1
else :
    result = int( a / (c - b) ) + 1
    
print(result)