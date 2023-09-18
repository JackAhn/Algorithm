t = int(input())

num = 0

while num < t :
    h, w, n = map(int, input().split())

    # ct = 0
    # floor = 0
    # roomnum = 0

    # for i in range(0, w) :
    #     roomnum += 1
    #     for j in range(0, h) :
    #         floor = j + 1
    #         ct += 1
    #         if ct == n :
    #             break
    #     if ct == n :
    #         break

    if(n % h == 0) :
        print( "{0:d}{1:02d}".format(h, int(n / h) ))
    else :
        print( "{0:d}{1:02d}".format(n % h , int((n / h)) + 1 ))


    #print( "{0:d}{1:02d}".format(floor, roomnum))
    num += 1