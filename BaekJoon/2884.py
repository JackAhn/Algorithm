h, m = input().split(' ')

h = int(h)
m = int(m)

if m >= 45 :
    m = m - 45
else :
    tmp = (60 + m) - 45
    m = tmp
    if h == 0 :
        h = 23
    else :
        h = h - 1
        
print('%d %d' % (h, m))