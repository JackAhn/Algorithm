h, m = input().split(' ')
plus = input()

h = int(h)
m = int(m)
plus = int(plus)

plush = int(plus / 60)
plusm = int(plus % 60)

h = h + plush
m = m + plusm

if m >= 60 :
    tmp = int(m / 60)
    h = h + tmp
    m = int(m % 60)

if h >= 24 :
    h = h - 24
    
print('%d %d' % (h, m))