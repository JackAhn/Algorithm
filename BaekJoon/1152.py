data = input()

if(data[0] == ' ') :
    data = data[1:]

if len(data) > 0 :
    data = data[:-1] if data[-1] == ' ' else data

result = 0
if len(data) > 0 :
    result = data.count(' ') + 1 if data.count(' ') > 0 else 1

print(result)