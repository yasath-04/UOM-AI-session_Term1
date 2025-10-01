def isPythTrip(a,b,c):
    data = [a, b, c]
    data.sort()

    if(data[0]**2 + data[1]**2 == data[2]**2):
        return True
    else:
        return False

def isSum1000(a,b,c):
    if(a+b+c == 1000):
        return True
    else:
        False

for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):
            if(isPythTrip(i,j,k) and isSum1000(i,j,k)):
                print((i, j, k))
                break

