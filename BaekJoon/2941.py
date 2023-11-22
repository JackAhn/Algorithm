s = input()

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for tmp in arr:
    s = s.replace(tmp, 't')

print(len(s))