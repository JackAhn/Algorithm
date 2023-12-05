while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    if n > m:
        print('multiple') if n % m == 0 else print('neither')
    else:
        print('factor') if m % n == 0 else print('neither')